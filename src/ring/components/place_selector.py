import streamlit as st
from ring.models.bird import Sighting
from collections import Counter

import pandas as pd

@st.fragment
def place_section(entry: Sighting | None = None, prefill: str = None):
    print("comp:place")
    data : list[Sighting] = st.session_state["data"]
    all_places = [entry.place for entry in data]
    place_counts = Counter(all_places)
    sorted_places = [place for place, _ in place_counts.most_common()]
    value = entry.place if entry else prefill
    if value not in sorted_places:
        sorted_places.append(value)
    st.selectbox(
        "Ort", sorted_places, key="field:place", index=sorted_places.index(value)
    )