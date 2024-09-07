import streamlit as st
from ring.sites.data.cache import get_sightings

st.set_page_config(layout="wide")


df = get_sightings()
st.table(df)
