import streamlit as st

pages = {
    "Erfassung": [
        st.Page("sites/new/add_sighting_simple.py", title="Neue Ablesung"),
        st.Page("sites/new/edit_sighting.py", title="Ablesung Bearbeiten"),
        st.Page("sites/new/edit_place.py", title="Ort Bearbeiten"),
    ],
    "Datenbank": [
        st.Page("sites/data/sightings.py", title="Ablesungen"),
        st.Page("sites/data/single_bird.py", title="Lebenslauf"),
    ],
    "Analyse": [
        st.Page("sites/analysis/main.py", title="Datenanalyse"),
    ],
}

pg = st.navigation(pages)
pg.run()
