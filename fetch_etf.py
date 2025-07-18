import requests
import json

session = requests.Session()
urltofetch = "https://www.nseindia.com/api/etf"

nseheaders = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Referer": "https://www.nseindia.com/market-data/exchange-traded-funds-etf",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-CH-UA": '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    "Sec-CH-UA-Mobile": "?0",
    "Sec-CH-UA-Platform": '"Windows"',
    "Cookie": "_ga=GA1.1.1833779144.1752831677; bm_mi=CE95F8ECD566CDF780CBD98ABB5A47D5~YAAQhqInF7/JYwiYAQAA27z7HBxAQIRDvBoFTMU+Nd36KFoLDJmydATTnLEa3jKfmmUVK0n9s+/K8QIAy+lrY9nBI35sjRnVdSHmPrBo6fXNUM8dXN7xYim07XHGmw4MHV/Jj+L/+PtbQKfReamgetAR0fY5qaz09IoCD91aIXWF/pqh7ighqFmdHLM8lV/GSW0o5Aej7IphUZLr2rzyrRzYKzVCOicME+fTDl5Z2o10T3q9Wdbj6PQyEEbJhm6DjSsfslihlZJd8wRxs8fmedhv4FIIUqIT75btGMGVW6DK9agP7LAQEvud+z6KoArM5l47F2VhPBBYbObcP1aJUmsUhgx0WOuzP4Umzvw8wsZM32g=~1; nsit=a5WxjvHBUc2iDzMER01Vkd1_; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTc1MjgzODYzNSwiZXhwIjoxNzUyODQ1ODM1fQ.xL5nj3TgPz0Un70ZHWVj8iTItNA8FobBaWLqgnwB30o; AKA_A2=A; ak_bmsc=DA91B12B6EAAC570275BB2ED0A6FB4E2~000000000000000000000000000000~YAAQFf7UFzQXCBmYAQAATP9SHRwTOcKfHVAqjhY9MLPHcWNxILblq0aGIHweFX/HoK0svvwQiyk0wMwcg3ywLhijJe3V8FTQikpYhHYfh/DZiz8jeE2lY/2jWKwCyMWapHZ1wtgGtgCfh7pBFgz7MSNRL9ZEjkBMPzKWFGk7Uek3H9r6dWyAJ+2JUnhY0sNtUtfzREAQWCXhfqXzlEtREyLvugTdovpfN43d7Dr2pEHX7taiXw7BoIZjIh/mwPSMOuFW+6jtVTnmms+Hhmbdp08TNr1zEjHaM9A/tx405QnmGoRx5IFSesLkH5k5iXbkXyIzyEbfjlhgf9HfRsAT11MDVj0u4oRPXiHtK/lfJ2wluk/OjzbEWTD3WvfEbJmABLoqcDrpiXxuLdFD9Xz6SxDwTRHmZ3j871ZEhw1WuZ3Qn6ZgNyqzyboOquhjB6PWU3lNxTX2rqS4qSoAHOFoq87aX6H/te/NC5gSVO1AOUIoP2AW9pSztS/hiOLnEU2Tua9MItDbwraHy3A1FmGDe5ICc5DTc54sQjIM6aRkn+Qhm25Z6Cs=; bm_sz=F03631F2FF298A6BE0EBEB157ED6045A~YAAQFf7UFzYXCBmYAQAATf9SHRwuI22Kpvpo1aSGQ3xqB7CWOsMjbxD1e5a4qcNFI+TPAhPi0+qAsJFE1gqLY0h5PdEhdEyBGXe1A0LatxmtJDTpUO7BeC+LixaCAdCev7x4LcKtIWr8Ln2khOc5SmlljALFdimju0lKJKqm4yYbkv4UdgF1CxD5OeDoSdNZoFsMWMf+d6WPRgfA4bk45k0y/TgoypIJeR59cPxF5shUWKCHug2kSE1/tKoOg9EuACnHCSjGB+TCqmi5ZULxFj2fj8qkrEs+lvNVAJxF4rVk+KS53K7pbVsHPUBcBVc83BpFkg6xysUZYPeTWXNOfWqIqmpFpOLYqe5myb5/+SwlULyk16j+XqkvGf4kJbT3kqRfg/d4bNs1jcm2jsc8MevzLEab6NtZzQy2mpVz9K1uwM56AcQY1LtoG5Of~3616825~4471093; _abck=AAB26DC180463194E7BB2B73150AFAAC~0~YAAQFf7UF0YXCBmYAQAAfABTHQ5Yzlvjjc/zju7zJgazGzCaIcsmXQppK7fdxvWoH4d5aGCnFN97KjXLJysdUGo8VciEWQzUKTAO0+kx+U3CKD5phR0iNarUq2wf5fm84rh4D4dsjmn4U9JWeVQhztRf7XjURrakiEHvYy2jHkRdrCYhL9ya8orwCQ9UKP7RbbgbH7SbLDZbwNnZMiZkPKNeJYa0bsL/VTJk8eDY6cFHOM9Ng8vVax9ewDYGQzINwXRWWQ0f0eKPY9nfzZovL4y9jx7ZAp36hFSU7aM5OtcpQ0e8t8rXz/vo5qG0cIA0aSrLRUpfEbOSGOMmPO6mTLbqag5VIsekTrjjgbwRdg8MaFTjq6BqaJjtRU/Ie9UpgPQwd49A2MkxE7yE9qZkAzmAsk6Qaiki4fv/tjsFuu1Vka9OTkKjZ3GqXRyinrgX7wEx2iozGZOMzmrBDYipNMVWlYeOpE9gQ9j49lU4ONundfm7ekeqMwVXDkNjmNZbmnEiXC8RD+CzOPnw/L3fSfZD7mLigILjeQxvU/VDDKX3kkno7pj/OCH/fEO/i3poY5ib44UNSvPX+Y/kz9xm9SdVKEKZMVAcn32zj4TbaNWy7iWjiR5dnqMCyXwcwjWST0CDMdtaxwVC8MA9SQBDPznRC282/hWdbK+dGVmO1y9qKsV8lv/nrk463eQT98AHLoDl0ug=~-1~-1~-1; RT="z=1&dm=nseindia.com&si=f486953c-23ad-41e3-ab7a-cde6f6c3cc44&ss=md8nglog&sl=0&se=8c&tt=0&bcn=%2F%2F684d0d47.akstat.io%2F"; bm_sv=6DE61A30EB85CA63EED445F16AC3E7DD~YAAQFf7UF3IXCBmYAQAAkgNTHRzrGN/7fNUYIfULXkMd3pNy0AxuFxCWCAKg2EAmEo6bCU7Iwb25WFKEzKmwrxJw82n31Wwtn5Iv2kfR2tFfoWWaA6hdcvcsO9itSKojr+tYd4IlNLpvqIt5RdxHHflurW2succ5Pdlug6kI+MHniTHdHqGBdML3SIb6PjVEVMGZ4rAbBhqlqFzc+QwXvGKLpHVb/7s4K8DtMJXeSx951tAlhy64GPzmMZa65JNFhypE~1; _ga_87M7PJ3R97=GS2.1.s1752838635$o2$g1$t1752838636$j59$l0$h0"

response = session.get(urltofetch, headers=nseheaders)
data = response.json()

# Optional: clean or restructure the `data['data']` if needed
with open("etf-data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
