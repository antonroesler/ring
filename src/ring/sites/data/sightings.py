import streamlit as st
from ring.sites.data.cache import get_sightings
from ring.db import Birds

st.set_page_config(page_title="Alle Ablesungen", layout="wide", page_icon="🦆")

df = get_sightings()

print(df.head())

event = st.dataframe(
    df,
    column_config={"Datum": st.column_config.DateColumn(format="DD.MM.YYYY")},
    use_container_width=True,
    hide_index=True,
    on_select="rerun",
    selection_mode="multi-row",
)

delete_btn = st.button(
    "Löschen", key="delete_btn", help="Löscht die ausgewählten Einträge"
)
edit_btn = st.button("Bearbeiten", key="edit_btn")

if delete_btn:
    if event.selection.rows:
        sightings = df.iloc[event.selection.rows]
        st.toast(f"{len(sightings)} Einträge gelöscht")
        # Delete the selected sightings from the database
        # for index, row in sightings.iterrows():
        unique_birds = sightings["Ringnummer"].unique()
        for bird in unique_birds:
            sightings_to_delete = sightings[sightings["Ringnummer"] == bird]
            print(f"Deleting {len(sightings_to_delete)}sightings from {bird}")
            sightings_ids = sightings_to_delete["id"].tolist()
            Birds.delete_sightings(bird, sightings_ids)
        df
