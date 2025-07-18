import requests
import json
from time import sleep
from datetime import datetime


def get_nse_session():
    """Initialize a session with NSE and set cookies to bypass 403 errors."""
    session = requests.Session()

    # Headers mimic a real Chrome browser
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
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
    }

    # Warm up session to set cookies
    try:
        resp = session.get("https://www.nseindia.com", headers=headers, timeout=10)
        if resp.status_code != 200:
            raise Exception("Failed to establish session.")
        sleep(1.5)
    except Exception as e:
        print("❌ Error initializing session:", e)
        return None

    return session


def fetch_etf_data(session):
    """Fetch ETF data from NSE using authenticated session."""
    api_url = "https://www.nseindia.com/api/etf"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/138.0.0.0 Safari/537.36",
        "Referer": "https://www.nseindia.com/market-data/exchange-traded-funds-etf",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Ch-Ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
    }

    try:
        resp = session.get(api_url, headers=headers, timeout=10)
        if resp.status_code == 200:
            return resp.json()
        else:
            print(f"❌ API request failed: {resp.status_code}")
            print("Text preview:", resp.text[:300])
    except requests.exceptions.RequestException as e:
        print("❌ Request error:", e)
    except json.JSONDecodeError as e:
        print("❌ JSON decode error:", e)

    return None


def save_data(data):
    """Save ETF data to a timestamped JSON file."""
    timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    filename = f"etf_data_{timestamp}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Saved ETF data to {filename}")


if __name__ == "__main__":
    session = get_nse_session()
    if session:
        data = fetch_etf_data(session)
        if data:
            save_data(data)
        else:
            print("⚠️ No data returned from NSE API.")
    else:
        print("❌ Could not initialize NSE session.")
