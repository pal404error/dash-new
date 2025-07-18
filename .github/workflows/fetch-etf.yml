import requests
import json
from time import sleep
from datetime import datetime

def get_valid_session():
    """Get a cookie-valid session for NSE API"""
    session = requests.Session()

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/138.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.nseindia.com",
        "Connection": "keep-alive",
        "Host": "www.nseindia.com",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
    }

    try:
        print("🔄 Visiting homepage to set cookies...")
        response = session.get("https://www.nseindia.com", headers=headers, timeout=10)
        if response.status_code == 200:
            print("✅ Cookie initialized")
            sleep(1.5)
            return session
        else:
            print("❌ Homepage request failed:", response.status_code)
    except Exception as e:
        print("❌ Exception in session init:", e)
    return None


def fetch_etf_data(session):
    api_url = "https://www.nseindia.com/api/etf"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/138.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.nseindia.com/market-data/exchange-traded-funds-etf",
        "Connection": "keep-alive",
        "Host": "www.nseindia.com",
        "X-Requested-With": "XMLHttpRequest",  # 🧠 KEY HEADER
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Ch-Ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
    }

    try:
        print("📡 Fetching ETF API data...")
        response = session.get(api_url, headers=headers, timeout=10)
        if response.status_code == 200:
            print("✅ Data fetched successfully")
            return response.json()
        else:
            print(f"❌ API request failed: {response.status_code}")
            print("Text preview:", response.text[:300])
    except Exception as e:
        print("❌ Exception fetching data:", e)

    return None


def save_data(data):
    timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    filename = f"etf_data_{timestamp}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Saved ETF data to {filename}")


if __name__ == "__main__":
    session = get_valid_session()
    if session:
        data = fetch_etf_data(session)
        if data:
            save_data(data)
        else:
            print("⚠️ No data received.")
    else:
        print("❌ Failed to initialize session.")
