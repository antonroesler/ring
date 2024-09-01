import streamlit as st
from ring.db.places import Places, Place


@st.dialog("Neuen Ort hinzufügen")
def new():
    name = st.text_input("Ort Name")
    lon = st.number_input("Longitude")
    lat = st.number_input("Latitude")
    desc = st.text_area("Beschreibung")
    if st.button("Speichern"):
        place = Place(name=name, lon=lon, lat=lat, desc=desc)
        Places().insert(place)
        st.session_state.new_place = place.name
        st.rerun()


if __name__ == "__main__":
    ...
