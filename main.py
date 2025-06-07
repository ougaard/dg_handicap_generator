import streamlit as st
import pandas as pd
from math import sqrt

from components import player_input, hero_box_ratings, advanced_settings

st.set_page_config(page_title="Disc Golf Handicap Calculator", page_icon="logo.png")

st.title("Disc Golf Handicap Calculator 🥏")
st.write("")


st.markdown(
    """
    <div style="
        background-color:#A8D5BA;
        padding:15px 20px;
        border-radius:12px;
        margin-bottom:20px;
        border: 1px solid #DDD;
    ">
    <h4 style="color:#333;">Estimate handicaps based on player ratings and course characteristics</h4>
    <p style="color:#333;">This app generates a handicap system for a group of players based on their UDisc ratings. 
    If a single player is entered, it outputs the expected score for that round.</p>
    </div>
    """,
    unsafe_allow_html=True
)
st.write()

st.markdown("#### Enter players and their UDisc ratings")
st.write("")

player_names, player_ratings = player_input()

with st.expander("Advanced Settings", expanded=False):
    c_1, c_2, b_ = advanced_settings()

def calculate_expected_score(rating):
    return (c_2 - sqrt(c_2**2 - 4 * c_1 * (b_-rating))) / (2*c_1)


_, c, _ = st.columns([3, 2, 3])
with c:
    generate = st.button("Calculate Handicaps", disabled=not all(player_names))

if generate:
    df = pd.DataFrame({
        "Player": player_names,
        "Rating": player_ratings,
    })
    df["Expected Score"] = [calculate_expected_score(r) for r in df["Rating"]]

    if len(player_names) > 1:
        anchor = df["Expected Score"].min()

        df["Handicap"] = [int(anchor - s - 0.3) for s in df["Expected Score"]]
        df = df.drop(columns=["Expected Score"])
    else:
        df["Expected Score"] = [round(s, 1) for s in df["Expected Score"]]


    st.markdown("---")
    st.markdown("### Calculated Player Handicaps")
    st.write("")

    st.dataframe(df, hide_index=True)