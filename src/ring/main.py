import streamlit as st

st.set_page_config(page_title="Vogelring", layout="wide", page_icon="🦆")

from ring.auth import get_current_user
from ring.models.user import Role


user = get_current_user()
pages = {}

if user is None:
    pages["Besucher"] = [
        st.Page("sites/new/add_sighting_simple.py", title="Ablesung Einreichen"),
        st.Page("sites/new/edit_sighting.py", title="Datenanfrage"),
    ]
elif user.role in [Role.USER, Role.OWNER, Role.ADMIN]:
    pages["Erfassung"] = [
        st.Page("sites/add_sightings.py", title="Neue Ablesung"),
    ]
    pages["Datenbank"] = [
        st.Page("sites/view_database.py", title="Datenbank"),
    ]

pg = st.navigation(pages)
pg.run()
