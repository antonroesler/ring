import streamlit as st
from ring.db import Places, Place


@st.dialog("Neuen Ort hinzufügen")
def new_place():
    name = st.text_input("Ort Name")
    lat = st.number_input("Latitude", value=50.110924, step=0.0005, format="%0.6f")
    lon = st.number_input("Longitude", value=8.682127, step=0.0005, format="%0.6f")
    url = "https://www.latlong.net/"
    st.markdown("[Koordinaten Finder](%s)" % url)
    desc = st.text_area("Beschreibung")
    if st.button("Speichern"):
        place = Place(name=name, lon=lon, lat=lat, desc=desc)
        Places.upsert(place)
        st.session_state["place_choice"] = [place.name] + st.session_state[
            "place_choice"
        ]
        st.rerun()


if __name__ == "__main__":
    ...
