import streamlit as st
import pandas as pd
from ring.models.bird import Sighting, LivingStatus, Habitat
from ring.data.saver import save_state
from ring.components.place_selector import place_section
from ring.components.date_picker import date_section
from ring import util


@st.fragment
def form(entry=None):
    """Edit Sighting. Excluding Place and Time."""
    if entry is None:
        entry = Sighting()
        st.markdown(f"*Neuer Eintrag wird erstellt*")
    else:
        i1, i2 = st.columns(2)
        with i1: 
            st.text(f"ID: {entry.id}")
        with i2: 
            st.markdown(f"Erstellungsdatum: {str(entry.creation_timestamp)}")

    reading_col1, reading_col2 = st.columns(2)
    with reading_col1:
        reading = st.text_input("Ablesung", value=entry.reading, key="field:reading")
    with reading_col2:
        color_reading = st.text_input("Ablesung (Farbring)", value=entry.reading_color_ring, key="field:color_reading")
    
    find_btn_col1, find_btn_col2 = st.columns(2)
    with find_btn_col1 :
        if st.button("Vogel Vorschlagen", use_container_width=True):
            st.session_state["suggested_ring"] = reading
            st.rerun(scope="fragment")

    individum_col1, individum_col2, individum_col3= st.columns(3) 
    with individum_col1: 
        ring = st.text_input("Ringnummer", value=entry.ring, key="field:ring")
    with individum_col2: 
        color_ring = st.text_input("Farbringnummer", value=entry.color_ring, key="field:color_ring")
    with individum_col3: 
        all_species = ["Graugans", "Möwe", None] # TODO: fetch species
        if entry.species not in all_species:
            all_species.append(entry.species)
        species = st.selectbox("Spezies", all_species, index=all_species.index(entry.species), key="field:species")
    
    r3_c1, r3_c2, r3_c3 = st.columns(3)
    with r3_c1: 
        partner = st.text_input("Partner", value=entry.partner, key="field:partner")
    with r3_c2: 
        sex_opts = ("M", "W", None)
        sex = st.selectbox("Geschlecht", options=sex_opts, index=sex_opts.index(entry.gender), key="field:sex")
    with r3_c3:
        age = st.text_input("Alter", value=entry.age, key="field:age")
    
    c1, c2, c3, c4 = st.columns(4)
    with c1: 
        group_size = st.number_input("Kleingruppengröße", min_value=0, max_value=100, step=1, value=entry.group or 0, key="field:group_size")
    with c2: 
        area_group_size = st.number_input("Gruppengröße", min_value=0, max_value=10000, step=10, value=entry.area_group or 0, key="field:area_group_size")
    with c3: 
        l_opts = [e.value for e in LivingStatus]
        living_type = st.selectbox("Typ", options=l_opts, index=l_opts.index(entry.living_type) or len(LivingStatus)-1, key="field:typ")
    with c4: 
        habitat_opts = [e.value for e in Habitat]
        habitat = st.selectbox("Habitat", options=habitat_opts, index=habitat_opts.index(entry.habitat) or len(Habitat)-1, key="field:habitat")
    comment = st.text_input("Kommentar", value=entry.comment, key="field:comment")
    melder = st.text_input("Melder", value=entry.melder, key="field:melder")
    melded = st.checkbox(label="Gemeldet", value=entry.melder, key="field:melded")




@st.dialog("Ablesung Bearbeiten", width="large")
def edit_sighting_entry(entry, index=None):
    btn = st.button("Speichern", use_container_width=True)
    place_section(entry)
    date_section(entry)
    form(entry)
    if btn:
        s = util.get_sighting_from_fields()
        if index:
            st.session_state["data"][index] = s
        save_state()
        st.rerun()
