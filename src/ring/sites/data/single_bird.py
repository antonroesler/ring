import streamlit as st
from ring.sites.data.cache import get_sightings

st.set_page_config(layout="wide")

ring_in = st.text_input("Ringnummer", key="search")
btn = st.button("Suchen", key="search_btn")


df = get_sightings()

if btn:
    df = df[df["Ringnummer"].str.contains(ring_in, na=False)]
    st.dataframe(df)
