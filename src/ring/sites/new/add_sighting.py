import streamlit as st
from streamlit_searchbox import st_searchbox
from ring.db import Species, Places, BirdSpecies, Birds, Bird, Sighting

st.set_page_config(layout="centered")

print("Running APP")
st.header("🔭 Neue Ablesung")

all_birds: list[Bird] = Birds.all()
all_rings = [b.id for b in all_birds]


with st.container():
    c1, c2 = st.columns(2)
    with c1:
        date_input = st.date_input("Date input", format="DD.MM.YYYY")
    with c2:
        time_input = st.time_input("Time entry")


all_places = Places.all()

place_select = st.selectbox(
    "Ort",
    [x.name for x in all_places],
    key="new_place",
)

st.button(
    "Neuer Ort",
    on_click=None,
)

all_species: list[BirdSpecies] = Species.all()


def search_rings() -> list[str]:
    print("Searching")
    searchterm = st.session_state.reading
    if len(searchterm) > 1:
        print(f"Searching for {searchterm}")
        st.session_state
        st.session_state["suggestions"] = [
            r for r in all_rings if searchterm.lower() in r.lower()
        ][:10]


reading = st.text_input(
    key="reading", placeholder="Ablesung", label="Ablesung", on_change=search_rings
)


suggestion_container = st.container()
if "suggestions" in st.session_state:
    with suggestion_container:
        for s in st.session_state.suggestions:
            st.write(s)

selected_species = st.selectbox(
    "Art",
    [f"{s.name} {f'- {s.name_latin}' if s.name_latin else ''}" for s in all_species],
    placeholder="Art auswählen",
    key="selected_species",
)


def save():
    ring_num = ring_input
    print(f"Saving {ring_num}")
    print(f"Species: {selected_species}")
    print(f"Place: {place_select}")
    Birds.add_sighting(
        bird_id=ring_num,
        sighting=Sighting(
            place=place_select,
            reading="",
            year=date_input.year,
            month=date_input.month,
            day=date_input.day,
            hour=time_input.hour,
            minute=time_input.minute,
        ),
    )


st.button("Speichern", type="primary", use_container_width=True, on_click=save)
