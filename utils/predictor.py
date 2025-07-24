import pandas as pd
import pickle

def load_model(model_path="models/model.pkl"):
    with open(model_path, "rb") as file:
        model = pickle.load(file)
    return model

def calculate_implied_probability(odds):
    return 1 / odds

def calculate_expected_value(prob, odds):
    return (prob * odds) - 1

def generate_ev_predictions(game_df, model):
    # Placeholder: use team name as dummy feature (you must replace this with real inputs)
    # This assumes you have already created a feature matrix (X)
    # For now, we simulate predictions randomly
    import numpy as np

    game_df["Predicted Win Prob"] = np.random.uniform(0.4, 0.6, size=len(game_df))  # Dummy probabilities
    game_df["Implied Prob"] = game_df["Odds"].apply(calculate_implied_probability)
    game_df["EV"] = game_df.apply(lambda row: calculate_expected_value(row["Predicted Win Prob"], row["Odds"]), axis=1)
    
    # Filter positive EV bets
    value_bets = game_df[game_df["EV"] > 0].sort_values(by="EV", ascending=False)
    return value_bets
