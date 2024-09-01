import streamlit as st

pages = {
    "Erfassung": [
        st.Page("sites/new/add_sighting.py", title="Neue Ablesung"),
        st.Page("sites/new/add-ringing.py", title="Neue Beringung"),
    ],
    "Datenbank": [
        st.Page("sites/data/sightings.py", title="Ablesungen"),
        st.Page("sites/data/places.py", title="Orte"),
        st.Page("sites/data/ringing.py", title="Beringungen"),
        st.Page("sites/data/species.py", title="Spezies"),
    ],
    "Analyse": [
        # st.Page("sites/analysis/learn.py", title="Datenanalyse"),
    ],
    "Hilfe": [
        st.Page("sites/chat/chat.py", title="KI Chat"),
    ],
}

pg = st.navigation(pages)
pg.run()
