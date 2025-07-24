# app.py — NBA Value Edge Dashboard

import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="NBA Value Edge", layout="wide")
st.title("🏀 NBA Value Edge")
st.subheader("Weekly AI-generated +EV NBA Bets")

@st.cache_data
def load_data():
    filepath = os.path.join("data", "ev_bets.csv")
    if os.path.exists(filepath):
        df = pd.read_csv(filepath)
        df = df.sort_values("EV", ascending=False)
        return df
    else:
        st.error("No EV bets found. Run weekly_runner.py to generate.")
        return pd.DataFrame()

df = load_data()

if not df.empty:
    st.markdown("### 📊 Filter by confidence, EV%, or team")
    min_ev = st.slider("Minimum EV %", 0.0, 50.0, 5.0, step=0.5)
    team_filter = st.text_input("Team filter (optional):", "")

    filtered = df[df['EV'] >= min_ev]
    if team_filter:
        filtered = filtered[filtered['Game'].str.upper().str.contains(team_filter.upper())]

    st.dataframe(filtered, use_container_width=True)
else:
    st.warning("No data available to display yet.")
