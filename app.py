
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="World Cup 2026 Sweepstake",
    page_icon="⚽",
    layout="wide"
)

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

st.markdown(
    """
    <h1 style='font-size:60px'>
    ⚽ World Cup 2026 Sweepstake
    </h1>
    """,
    unsafe_allow_html=True
)

selected = option_menu(
    menu_title=None,
    options=[
        "Fixtures & Results",
        "Group Tables",
        "Knockouts",
        "WhatsApp",
        "Who Owns What"
    ],
    icons=[
        "calendar-event",
        "table",
        "trophy",
        "whatsapp",
        "people-fill"
    ],
    orientation="horizontal",
    default_index=4
)

if selected == "Who Owns What":

    st.subheader("Team Ownership")

    for player, teams in participants.items():

        with st.expander(player):

            for team in teams:
                st.write(f"⚽ {team}")

elif selected == "WhatsApp":

    st.subheader("WhatsApp Group")

    st.info(
        "Paste your WhatsApp invite link here."
    )

elif selected == "Fixtures & Results":

    st.subheader("Fixtures & Results")

    st.info(
        "World Cup fixtures will appear here."
    )

elif selected == "Group Tables":

    st.subheader("Group Tables")

    st.info(
        "Group standings will appear here."
    )

elif selected == "Knockouts":

    st.subheader("Knockout Stage")

    st.info(
        "Knockout bracket will appear here."
    )
```
