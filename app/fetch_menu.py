from curl_cffi import requests
from datetime import datetime
from typing import List,Dict

BASE_URL = "https://apiv4.dineoncampus.com"
LOCATION_ID = "5b10d972f3eeb60909e01489"
HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Origin": "https://dineoncampus.com",
    "Referer": "https://dineoncampus.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
}

def get_today_date()->str:
    return datetime.now().strftime("%Y-%m-%d")

def get_periods(date_str:str)->List[Dict]:
    url = f"{BASE_URL}/locations/{LOCATION_ID}/periods/"
    params = {"date":date_str}
    response = requests.get(url,params=params,headers=HEADERS,timeout=30,impersonate="chrome")
    response.raise_for_status()
    return response.json().get("periods",[])

def get_menu(date_str:str,period_id:str)-> Dict:
    url = f"{BASE_URL}/locations/{LOCATION_ID}/menu"
    params ={"date":date_str,"period":period_id}
    response = requests.get(url,params=params,headers=HEADERS,timeout=30,impersonate="chrome")
    response.raise_for_status()
    return response.json()

def fetch_all_menus(date_str:str)->Dict[str,Dict]:
    periods = get_periods(date_str)
    all_menus = {}
    for period in periods:
        name = period.get("name")
        slug = period.get("slug")
        period_id = period.get("id")
        
        print(f"Fetching {name}...")
        menu_data = get_menu(date_str, period_id)
        
        all_menus[slug] = {
            "name":name,
            "slug":slug,
            "period_id": period_id,
            "data": menu_data,
        }
        
    return all_menus        

def main():
    date_str = get_today_date()
    print(f"\nFetching menus for {date_str}\n")
    all_menus = fetch_all_menus(date_str)
    for slug,content in all_menus.items():
        categories = content["data"].get("period",{}).get("categories",[])
        total_items = sum(len(cat.get("items", [])) for cat in categories)
        print(f"{slug.upper()} → {total_items} items")
    print("\nFetch complete.\n")

if __name__ == "__main__":
    main()