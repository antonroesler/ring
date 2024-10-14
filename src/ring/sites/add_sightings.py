import streamlit as st
from ring.components.add_sighting import sighting_entry
import pandas as pd

print("Site: add_sightings")
st.header("🔭 Neue Ablesung")

if "new_records" not in st.session_state:
    st.session_state["new_records"] = dict()

with st.container():
    c1, c2 = st.columns(2)
    with c1:
        date_input = st.date_input("Datum", format="DD.MM.YYYY")
    with c2:
        time_input = st.time_input("Uhrzeit")


all_places = ["Frankfurt", "Offenbach"]  # TODO: fetch places

if "place_choice" not in st.session_state:
    st.session_state["place_choice"] = all_places
place_select = st.selectbox(
    "Ort", st.session_state["place_choice"], key="new_place", index=0
)

st.button(
    "Neue Ablsung",
    use_container_width=True,
    on_click=sighting_entry,
    kwargs={"gid": len(st.session_state["new_records"]) + 1},
)


for k, df in st.session_state["new_records"].items():
    st.markdown(f"**Gruppe {k}**")
    st.button(
        "Weiteren Vogel zu Gruppe Hinzufügen",
        use_container_width=True,
        on_click=sighting_entry,
        kwargs={"gid": k},
        key=f"{k}add",
    )
    st.dataframe(df)
