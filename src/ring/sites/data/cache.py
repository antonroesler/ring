from ring.db import Birds, Bird, Sighting, Places, Place
import pandas as pd
import streamlit as st

from datetime import date


@st.cache_data(ttl=600)
def _get_data(refresh=False) -> list[Bird]:
    print("Actually fetching data")
    return Birds.all()


@st.cache_data(ttl=600)
def get_sightings(refresh=False):
    print("Fetching ALL data")
    data: list[Bird] = _get_data(refresh)

    def add(sighting: Sighting, bird: Bird):
        return {
            "Art": bird.species,
            "Ringnummer": bird.id,
            "Geschlecht": bird.gender,
            "Partner": bird.partner,
            "Ablesung": sighting.reading,
            "Ort": sighting.place,
            "Datum": date(year=sighting.year, month=sighting.month, day=sighting.day),
            "Melder": sighting.melder,
            "Bemerkung": sighting.comment,
            "Gruppengröße": int(float(sighting.area_group))
            if sighting.area_group
            else None,
            "Kleingruppengröße": int(float(sighting.group)) if sighting.group else None,
            "Habitat": sighting.habitat,
            "Typ": sighting.living_type,
            "id": sighting.id,
        }

    sightings = [add(s, b) for b in data for s in b.sightings]

    return pd.DataFrame(sightings)


@st.cache_data(ttl=600)
def get_individuals():
    data: list[Bird] = _get_data()

    return pd.DataFrame(
        [
            {
                "Art": bird.species,
                "Ringnummer": bird.id,
                "Ablesungen": len(bird.sightings),
            }
            for bird in data
        ]
    )


@st.cache_data(ttl=600)
def get_places():
    data: list[Place] = Places.all()
    return {p.name: p for p in data}
