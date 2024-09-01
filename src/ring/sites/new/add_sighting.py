import streamlit as st
from ring.db.places import Places, Place
from ring.db.sighting import Sighting, Sightings
from ring.db.rings import Rings, Ring
from ring.db.species import Species, BirdSpecies
from ring.sites.new.places import new as new_place

st.set_page_config(layout="centered")

st.header("🔭 Neue Ablesung")


with st.container():
    c1, c2 = st.columns(2)
    with c1:
        date_input = st.date_input("Date input", format="DD.MM.YYYY")
    with c2:
        time_input = st.time_input("Time entry")


all_places = Places().all()
print(all_places)

place_select = st.selectbox(
    "Ort",
    [x.name for x in all_places],
    key="new_place",
)

st.button(
    "Neuer Ort",
    on_click=new_place,
)

all_species: list[BirdSpecies] = Species().all()

selected_species = st.selectbox(
    "Art",
    [f"{s.name} - {s.name_latin}" for s in all_species],
    placeholder="Art auswählen",
)


ring_input = st.text_input("Ring Nummer")


def save():
    Rings().insert(Ring(num=ring_input, species=selected_species))

    sighting = Sighting(
        ring=ring_input,
        place=place_select,
        species=selected_species.split(" - ")[0],
        year=date_input.year,
        month=date_input.month,
        day=date_input.day,
        hour=time_input.hour,
        minute=time_input.minute,
    )
    Sightings().insert(sighting)
    st.toast(
        f"Ablesung {selected_species} {ring_input} in {place_select} gespeichert",
        icon="🦆",
    )


st.button("Speichern", type="primary", use_container_width=True, on_click=save)
