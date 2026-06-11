# app.py

import streamlit as st
import pandas as pd

st.set_page_config(page_title="World Cup 2026 Sweepstake", page_icon="🏆", layout="wide")

PRIZE_POOL = 100

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

scores = {
"Cabecinha": 0,
"Gui": 0,
"Marcão": 0,
"Bruno": 0,
"Negão": 0,
"Bob": 0,
"Bila": 0,
"Salim": 0,
"Léo": 0,
"Victor": 0
}

st.title("🏆 World Cup 2026 Sweepstake")

tab1, tab2, tab3, tab4 = st.tabs([
"Leaderboard",
"Teams",
"Prize Pool",
"Draw Results"
])

with tab1:
st.subheader("Leaderboard")

```
leaderboard = pd.DataFrame(
    [{"Player": k, "Points": v} for k, v in scores.items()]
)

leaderboard = leaderboard.sort_values(
    by="Points",
    ascending=False
)

st.dataframe(
    leaderboard,
    use_container_width=True,
    hide_index=True
)
```

with tab2:
st.subheader("Teams")

```
for player, teams in participants.items():
    with st.expander(player):
        for team in teams:
            st.write(f"⚽ {team}")
```

with tab3:
st.subheader("Prize Pool")

```
st.metric(
    "Total Prize Pool",
    f"£{PRIZE_POOL}"
)

st.write("🥇 Champion: 70%")
st.write("🥈 Runner-up: 20%")
st.write("💩 Worst Team Out First: 10%")

st.write("")
st.write(f"Champion: £{PRIZE_POOL * 0.70:.0f}")
st.write(f"Runner-up: £{PRIZE_POOL * 0.20:.0f}")
st.write(f"Worst Team Out First: £{PRIZE_POOL * 0.10:.0f}")
```

with tab4:
st.subheader("Draw Results")

```
for player, teams in participants.items():
    st.markdown(f"### {player}")
    st.write(", ".join(teams))
    st.divider()
```

st.sidebar.title("World Cup 2026")

st.sidebar.info(
"""
Participants: 10

```
Teams: 48

Format:
4 Pots

Champion: 70%
Runner-up: 20%
Worst Team Out First: 10%
"""
```

)
