from fetch_menu import get_today_date,fetch_all_menus
from normalize import normalize_menu
from db import init_db, save_menu_items

def run_pipeline():
    date = get_today_date()
    print(f"Processing Food menu for {date}")
    all_menu = fetch_all_menus(date_str=date)
    normalized_items = normalize_menu(all_menu,date)
    print(f"Normalized Menu {len(normalized_items)} items")
    init_db()
    save_menu_items(normalized_items)
    print("Data saved to Database")
    
if __name__ == "__main__":
    run_pipeline()
    