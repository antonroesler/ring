import streamlit as st
from ring.components.add_sighting import sighting_entry
import pandas as pd
from ring.models.bird import Sighting
import random
import string
import numbers
from datetime import datetime
from ring.data.loader import load_data
from ring.components.edit_sighting import edit_sighting_entry


print("Site: view_database")
st.header("Datenbank")


if st.session_state.get("data") is None:
    st.session_state["data"] = load_data()

df = st.dataframe(
    pd.DataFrame(
        data=[obj.model_dump(by_alias=True) for obj in st.session_state["data"]],
    ),
    selection_mode="single-row",
    key="selected_sighting",
    on_select="rerun",
    use_container_width=True,
    hide_index=True,
    column_config={"Datum": st.column_config.DateColumn(format="DD.MM.YYYY")},
    column_order=[
        "Ringnummer",
        "Datum",
        "Art",
        "Ort",
        "Ablesung",
        "Farbring",
        "Ablesung (Farbring)",
        "Geschlecht",
        "Alter",
        "Partner",
        "Kleingruppengröße",
        "Gruppengröße",
        "Habitat",
        "Typ",
        "Kommentar",
        "Melder",
        "Gemeldet",
        "Gruppen ID",
    ],
)

if st.button("Ablesung Bearbeiten"):
    st.text(st.session_state["data"][df.selection.rows[0]])
    edit_sighting_entry(st.session_state["data"][df.selection.rows[0]], df.selection.rows[0])
