import streamlit as st
from ring.auth import get_current_user
from ring.db.user import Role

st.set_page_config(page_title="Vogelring", layout="centered", page_icon="🦆")

user = get_current_user()
pages = {
    "Nutzerverwaltung": [
        st.Page("sites/auth/users.py", title="Nutzer"),
    ]
}

if user is None:
    pages["Besucher"] = [
        st.Page("sites/new/add_sighting_simple.py", title="Ablesung Einreichen"),
        st.Page("sites/new/edit_sighting.py", title="Datenanfrage"),
    ]
elif user.role in [Role.USER, Role.OWNER, Role.ADMIN]:
    pages["Erfassung"] = [
        st.Page("sites/new/add_sighting_simple.py", title="Neue Ablesung"),
        st.Page("sites/new/edit_sighting.py", title="Ablesung Bearbeiten"),
        st.Page("sites/new/edit_place.py", title="Ort Bearbeiten"),
    ]
    pages["Datenbank"] = [
        st.Page("sites/data/sightings.py", title="Ablesungen"),
        st.Page("sites/data/single_bird.py", title="Lebenslauf"),
    ]
    pages["Analyse"] = [
        st.Page("sites/analysis/main.py", title="Datenanalyse"),
    ]
    pages["Debug"] = [
        st.Page("header.py", title="Header"),
    ]


pg = st.navigation(pages)
pg.run()
