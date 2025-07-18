import requests
import json

session = requests.Session()
url = "https://www.nseindia.com/api/cmsNote?url=exchange-traded-funds-etf"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Referer": "https://www.nseindia.com/market-data/exchange-traded-funds-etf",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Ch-Ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\""
}

r = session.get(url, headers=headers)
data = r.json()

# Optional: clean or restructure the `data['data']` if needed
with open("etf-data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
