import streamlit as st
from datetime import datetime, date, time

def get_date():
    date_part: date | None = st.session_state.get("field:date")
    time_part: time | None = st.session_state.get("field:time")
    if date_part is not None:
        h, m = 12, 0
        if time_part is not None:
            h = time_part.hour
            m = time_part.minute
        return datetime(year=date_part.year, month=date_part.month, day=date_part.day, hour=h, minute=m)
    return None
