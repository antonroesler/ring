import streamlit as st
from ring.components.add_sighting import sighting_entry
import pandas as pd
from ring.models.bird import Sighting
import random
import string
import numbers
from datetime import datetime
from ring.components.edit_sighting import edit_sighting_entry
from ring import util

print("Site: view_database")
st.header("Datenbank")


df = util.get_df(st.session_state["data"])

if st.button("Ablesung Bearbeiten"):
    st.text(st.session_state["data"][df.selection.rows[0]])
    edit_sighting_entry(st.session_state["data"][df.selection.rows[0]], df.selection.rows[0])
