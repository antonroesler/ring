import streamlit as st
from ring.db.sighting import Sighting, Sightings
from ring.db.rings import Rings, Ring
import pandas as pd

st.set_page_config(layout="wide")

all_sightings = Sightings().all()
all_rings = Rings().all()
ring_map = {r.num: r for r in all_rings}


def get_species(ring: str):
    r = ring_map.get(ring)
    if r is None:
        return "Unknown"
    return r.species


data = [
    {
        "Ringnummer": s.ring,
        "Art": get_species(s.ring),
        "Ort": s.place,
        "Datum": f"{s.day}.{s.month}.{s.year} {s.hour}:{s.minute}",
    }
    for s in all_sightings
]


st.table(data)
