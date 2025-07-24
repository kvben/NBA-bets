import requests
import pandas as pd


API_KEY = "cc3b6e75f2fb83f5645bc1d971108b1b"
REGION = "us"
SPORT = "basketball_nba"
MARKET = "h2h"  # head-to-head (moneyline)

def fetch_upcoming_games_with_odds():
    url = f"https://api.the-odds-api.com/v4/sports/{SPORT}/odds"
    params = {
        "apiKey": API_KEY,
        "regions": REGION,
        "markets": MARKET,
        "oddsFormat": "decimal"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception(f"API Error: {response.status_code} - {response.text}")

    odds_data = response.json()

    rows = []
    for game in odds_data:
        if not game.get("bookmakers"):
            continue

        bookmaker = game["bookmakers"][0]
        outcomes = bookmaker["markets"][0]["outcomes"]

        for outcome in outcomes:
            rows.append({
                "Game": f"{game['home_team']} vs {game['away_team']}",
                "Team": outcome["name"],
                "Odds": outcome["price"]
            })

    df = pd.DataFrame(rows)
    return df
