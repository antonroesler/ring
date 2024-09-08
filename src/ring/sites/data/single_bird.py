import streamlit as st
from ring.sites.data.cache import get_sightings

st.set_page_config(page_title="Lebenslauf", layout="wide", page_icon="🦆")

ring_in = st.text_input("Ringnummer", key="search")
btn = st.button("Suchen", key="search_btn")


df = get_sightings()

if btn:
    df = df[df["Ringnummer"].str.contains(ring_in, na=False)]
    st.dataframe(
        df, column_config={"Datum": st.column_config.DateColumn(format="DD.MM.YYYY")}
    )
