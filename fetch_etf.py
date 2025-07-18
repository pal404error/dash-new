import requests
import json
from time import sleep
from datetime import datetime

# Step 1: Initialize a session
session = requests.Session()

# Step 2: Basic headers
base_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.nseindia.com",
}

# Step 3: Trigger homepage to get cookies
session.get("https://www.nseindia.com", headers=base_headers)
sleep(1)

# Step 4: Fetch ETF data
api_url = "https://www.nseindia.com/api/etf"
api_headers = {
    **base_headers,
    "Referer": "https://www.nseindia.com/market-data/exchange-traded-funds-etf",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-CH-UA": '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    "Sec-CH-UA-Mobile": "?0",
    "Sec-CH-UA-Platform": '"Windows"',
}

response = session.get(api_url, headers=api_headers)

# Step 5: Save response to JSON
if response.ok:
    try:
        data = response.json()
        timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
        filename = f"etf_data_{timestamp}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"Saved ETF data to {filename}")
    except Exception as e:
        print("Failed to parse JSON:", e)
else:
    print("Failed to fetch ETF data:", response.status_code, response.text)
