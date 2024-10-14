import streamlit as st
from datetime import datetime, time
from ring.models.bird import Sighting

st.fragment
def date_section(entry: Sighting | None = None, prefill: datetime | None = None):
    value = entry.date if (entry and entry.date) else prefill
    with st.container():
        c1, c2 = st.columns(2)
        with c1:
            st.date_input("Datum", format="DD.MM.YYYY", key="field:date", value=value)
        with c2:
            st.time_input("Uhrzeit", key="field:time", value=value if value else time(hour=12))