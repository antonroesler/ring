import streamlit as st
from ring.models import (
    Birds,
    Bird,
)


print("Running APP")
st.header("✏️ Ablesung Bearbeiten")

ring_num = st.text_input("Ringnummer", key="ring_num")
btn = st.button("Suchen", key="search_btn")

if btn:
    bird: Bird | None = Birds.get(ring_num)
    if bird:
        for s in bird.sightings:
            st.write(f"{s.day}.{s.month}.{s.year} {s.reading} {s.place}")
            st.button("Bearbeiten", key=f"edit_{s.id}")
