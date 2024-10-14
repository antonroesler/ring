import streamlit as st
from ring.models.bird import Sighting
from ring import util

def get_sighting_from_fields():
    return Sighting(
            ring=st.session_state["field:ring"],
            color_ring=st.session_state["field:color_ring"],
            reading=st.session_state["field:reading"],
            place=st.session_state["field:place"],
            date=util.get_date(),
            reading_color_ring=st.session_state["field:color_reading"],
            species=st.session_state["field:species"],
            gender=st.session_state["field:sex"],
            age=st.session_state["field:age"],
            partner=st.session_state["field:partner"],
            group=st.session_state["field:group_size"],
            area_group=st.session_state["field:area_group_size"],
            habitat=st.session_state["field:habitat"],
            living_type=st.session_state["field:typ"],
            comment=st.session_state["field:comment"],
            melder=st.session_state["field:melder"],
            melded=st.session_state["field:melded"],
        )
