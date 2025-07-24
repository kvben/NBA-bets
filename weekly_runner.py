import os
import pandas as pd
from utils.nba_scraper import fetch_upcoming_games_with_odds
from utils.predictor import load_model, predict_ev

def run_pipeline():
    os.makedirs("data", exist_ok=True)

    print("[1] Fetching upcoming games and odds...")
    games = fetch_upcoming_games_with_odds()
    print(f"Fetched {len(games)} games.")

    print("[2] Loading prediction model...")
    model = load_model("models/model.pkl")

    print("[3] Predicting EV values...")
    results = predict_ev(model, games)
    results.to_csv("data/ev_bets.csv", index=False)
    print("✅ EV Bets saved to data/ev_bets.csv")

if __name__ == "__main__":
    run_pipeline()
