import streamlit as st
import time
from ring.db import Places, Place

st.set_page_config(page_title="Ort Bearbeiten", layout="wide", page_icon="✏️")

st.header("✏️ Ort Bearbeiten")


@st.cache_data(ttl=600)
def get_places() -> list[Place]:
    return [
        {"id": p.id, "name": p.name, "lat": p.lat, "lon": p.lon} for p in Places.all()
    ]


all_places = get_places()

col1, col2 = st.columns(2)

with col1:
    frame = st.dataframe(
        all_places,
        use_container_width=True,
        hide_index=True,
        on_select="rerun",
        selection_mode="single-row",
        column_config={
            "lon": st.column_config.NumberColumn(),
            "lat": st.column_config.NumberColumn(),
        },
        column_order=["name", "lat", "lon"],
    )

with col2:
    if frame.selection.rows:
        _data: Place = all_places[frame.selection.rows[0]]
        data: Place = Places.get(_data["id"])
        st.write("Ort Bearbeiten")
        st.write(data.name)
        new_lat = st.number_input(
            "Latitude", value=data.lat, step=0.0005, format="%0.6f"
        )
        new_lon = st.number_input(
            "Longitude", value=data.lon, step=0.0005, format="%0.6f"
        )
        btn = st.button("Speichern")
        if btn:
            print("Saving")
            p = Place(id=data.id, name=data.name, lat=new_lat, lon=new_lon)
            Places.upsert(p)
            st.success(
                f"{data.name} gespeichert.\nLatitude: {new_lat}\nLongitude: {new_lon}",
                icon="📍",
            )
            time.sleep(1)
            st.rerun()
