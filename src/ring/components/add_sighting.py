import streamlit as st
import pandas as pd
from ring import util
from ring.components.edit_sighting import form 
from ring.data.saver import save_state

def _get_group(gid) -> list:
    if gid not in st.session_state["new_records"]:
        st.session_state["new_records"][gid] = list()
    return st.session_state["new_records"][gid]


@st.dialog("Neue Ablesung Eingeben", width="large")
def sighting_entry(gid):
    btn = st.button("Speichern", use_container_width=True)
    form()
    if btn:
        s = util.get_sighting_from_fields()
        group = _get_group(gid)
        s.sighting_group_id = int(str(id(group))+str(gid))
        group.append(s)
        st.session_state["data"].append(s)
        save_state()
        st.rerun(scope="app")