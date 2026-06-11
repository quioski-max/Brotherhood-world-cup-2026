import streamlit as st
import pandas as pd

st.set_page_config(page_title="World Cup 2026 Sweepstake", page_icon="🏆")

participants = {
    "Cabecinha": ["England", "Norway", "Türkiye", "Qatar"],
    "Gui": ["Spain", "Uruguay", "Canada", "Haiti", "Panama"],
    "Marcão": ["Croatia", "Morocco", "South Korea", "Australia", "Ivory Coast"],
    "Bruno": ["Germany", "United States", "South Africa", "Jordan", "Iran"],
    "Negão": ["Portugal", "Colombia", "Saudi Arabia", "Curaçao", "Algeria"],
    "Bob": ["Netherlands", "Sweden", "Czech Republic", "New Zealand", "Paraguay"],
    "Bila": ["Belgium", "Japan", "Tunisia", "Cape Verde", "Iraq"],
    "Salim": ["Argentina", "Mexico", "Scotland", "DR Congo"],
    "Léo": ["France", "Austria", "Egypt", "Bosnia & Herzegovina", "Senegal"],
    "Victor": ["Brazil", "Switzerland", "Ghana", "Uzbekistan", "Ecuador"]
}

st.title("🏆 Brotherhood World Cup 2026")

tab1, tab2 = st.tabs(["Leaderboard", "Teams"])

with tab1:
    leaderboard = pd.DataFrame(
        [{"Player": p, "Points": 0} for p in participants.keys()]
    )
    st.dataframe(leaderboard, use_container_width=True)

with tab2:
    for player, teams in participants.items():
        st.subheader(player)
        for team in teams:
            st.write("⚽", team)
