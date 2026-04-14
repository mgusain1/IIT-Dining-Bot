from curl_cffi import requests

url = "https://apiv4.dineoncampus.com/locations/5b10d972f3eeb60909e01489/periods/"
params = {"date": "2026-04-01"}

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Origin": "https://dineoncampus.com",
    "Referer": "https://dineoncampus.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
}

response = requests.get(
    url,
    params=params,
    headers=headers,
    impersonate="chrome",
    timeout=30
)

print("STATUS:", response.status_code)
print(response.text[:500])