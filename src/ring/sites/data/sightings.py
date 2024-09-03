import streamlit as st
from ring.db.sighting import Sighting, Sightings
from ring.db.rings import Rings, Ring
from ring.db.places import Places, Place
from ring.db.species import Species, Species
import pandas as pd

st.set_page_config(layout="wide")

all_sightings = Sightings().all()
all_rings = Rings().all()
all_species = Species().all()
all_places = Places().all()

species_map = {s.id: s for s in all_species}
place_map = {p.id: p for p in all_places}
ring_map = {r.id: r for r in all_rings}


def get_species(id: str):
    r = species_map.get(id)
    if r is None:
        return "Unknown"
    return r.name


def get_place(id: str):
    r = place_map.get(id)
    if r is None:
        return "Unknown"
    return r.name


def get_ring(id: str):
    r = ring_map.get(id)
    if r is None:
        return "Unknown"
    return r.num


data = [
    {
        "Ringnummer": get_ring(s.ring),
        "Art": get_species(ring_map.get(s.ring).species),
        "Ort": get_place(s.place),
        "Datum": f"{s.day}.{s.month}.{s.year} {s.hour}:{s.minute}",
    }
    for s in all_sightings
]


st.table(data)
