"""Streamlit view. Keep it thin: load state, call poll.core, render."""

import altair as alt
import pandas as pd
import streamlit as st

from poll import store
from poll.core import create_poll, format_share, leaders, shares, tally, total_votes, vote

st.set_page_config(page_title="Live Poll", page_icon="🗳️")
st.title("🗳️ Live Poll")

poll = store.load()

if poll is None:
    st.subheader("Create a poll")
    with st.form("create"):
        question = st.text_input("Question")
        options_text = st.text_area("Options, one per line")
        submitted = st.form_submit_button("Create poll")
    if submitted:
        try:
            store.save(create_poll(question, options_text.splitlines()))
        except ValueError as err:
            st.error(str(err))
        else:
            st.rerun()
    st.stop()

st.subheader(poll["question"])

with st.form("vote"):
    choice = st.radio("Your vote", poll["options"])
    if st.form_submit_button("Vote"):
        store.save(vote(poll, choice))
        st.rerun()

results = pd.DataFrame(tally(poll), columns=["Option", "Votes"])
results["Share"] = [format_share(percent) for _, percent in shares(poll)]
leading = set(leaders(poll))
results["Leader"] = ["🏆" if option in leading else "" for option in results["Option"]]

text_color = "#fafafa" if st.context.theme.type == "dark" else "#31333f"
bars = alt.Chart(results).encode(
    x=alt.X("Option:N", sort=None, axis=alt.Axis(labelAngle=0)),
    y=alt.Y("Votes:Q", axis=alt.Axis(tickMinStep=1)),
)
chart = (
    bars.mark_bar()
    + bars.mark_text(baseline="bottom", dy=-4, color=text_color).encode(text="Share:N")
    + bars.mark_text(baseline="bottom", dy=-22, fontSize=18, color=text_color).encode(
        text="Leader:N"
    )
).properties(padding={"top": 30})
st.altair_chart(chart)
st.caption(f"{total_votes(poll)} votes so far")

if st.button("Reset poll"):
    store.clear()
    st.rerun()
