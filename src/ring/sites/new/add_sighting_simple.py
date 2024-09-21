import streamlit as st
from ring.db import (
    Species,
    Places,
    BirdSpecies,
    Birds,
    Bird,
    Sighting,
    LivingType,
    Habitat,
)
from ring.sites.new.places import new_place
from ring.sites.new.find_bird import find_bird

print("Running APP")
st.header("🔭 Neue Ablesung")


with st.container():
    c1, c2 = st.columns(2)
    with c1:
        date_input = st.date_input("Date input", format="DD.MM.YYYY")
    with c2:
        time_input = st.time_input("Time entry")


all_places = Places.all()

place_choice = [x.name for x in all_places]
if "place_choice" not in st.session_state:
    st.session_state["place_choice"] = place_choice


place_select = st.selectbox(
    "Ort", st.session_state["place_choice"], key="new_place", index=0
)

bcol1, bcol2, _1, _2 = st.columns(4)
with bcol1:
    st.button("Neuer Ort", on_click=new_place, use_container_width=True)
with bcol2:
    st.button("Vogel Finden", on_click=find_bird, use_container_width=True)

all_species: list[BirdSpecies] = Species.all()


ring_col1, ring_col2, ring_col3 = st.columns(3)
with ring_col1:
    reading = st.text_input(key="reading", placeholder="Ablesung", label="Ablesung")
with ring_col2:
    ring_num = st.text_input(key="ringnum", placeholder="Ring Nummer", label="Ring")
with ring_col3:
    idx = 0
    opts = ["-"] + [
        f"{s.name} {f'- {s.name_latin}' if s.name_latin else ''}".strip()
        for s in all_species
    ]
    if st.session_state.get("find_species"):
        idx = opts.index(st.session_state["find_species"])

    selected_species = st.selectbox(
        "Art", opts, placeholder="Art auswählen", key="selected_species", index=idx
    )

col1, col2, col3, col4 = st.columns(4)

with col1:
    selected_habitat = st.selectbox(
        "Habitat",
        [h.value for h in Habitat],
        key="selected_habitat",
        index=len(Habitat) - 1,
    )
with col2:
    selected_living_type = st.selectbox(
        "Typ",
        [l.value for l in LivingType],
        key="selected_living_type",
        index=len(LivingType) - 1,
    )
with col3:
    group_size = st.number_input(
        "Kleingruppengröße", min_value=1, value=1, max_value=50
    )
with col4:
    area_group_size = st.number_input(
        "Gruppengröße", min_value=1, value=1, max_value=1000
    )

mcol1, mcol2 = st.columns(2)
with mcol1:
    melder = st.text_input(key="melder", placeholder="Melder", label="Melder")
with mcol2:
    melded = st.radio(
        key="melded", label="Gemeldet", options=["Ja", "Nein"], horizontal=True
    )

bemerkung = st.text_area(key="bemerkung", placeholder="Bemerkung", label="Bemerkung")


def save():
    if selected_species == "-":
        st.error("Bitte Art auswählen")
        return
    existing: Bird | None = Birds.get(ring_num)
    print(f"Existing: {existing}")
    if existing:
        if existing.species != selected_species:
            st.error(f"{ring_num} existiert bereits als {existing.species}")
            return
    print(f"Saving {ring_num}")
    print(f"Species: {selected_species}")
    print(f"Place: {place_select}")
    Birds.add_sighting(
        bird_id=ring_num.strip(),
        species=selected_species.strip(),
        sighting=Sighting(
            place=place_select.strip(),
            reading=reading.strip(),
            year=date_input.year,
            month=date_input.month,
            day=date_input.day,
            hour=time_input.hour,
            minute=time_input.minute,
            habitat=Habitat(selected_habitat),
            living_type=LivingType(selected_living_type),
            group=group_size,
            area_group=area_group_size,
            melder=melder.strip(),
            melded=melded == "Ja",
            comment=bemerkung,
        ),
    )
    st.toast(f"Gespeichert: {selected_species} in {place_select}", icon="🦆")
    st.session_state["find_species"] = "-"
    st.session_state["reading"] = None
    st.session_state["ringnum"] = None


st.button("Speichern", type="primary", use_container_width=True, on_click=save)
