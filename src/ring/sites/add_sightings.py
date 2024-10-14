import streamlit as st
from ring.components.add_sighting import sighting_entry
from ring.components.place_selector import place_section
from ring.components.date_picker import date_section
import pandas as pd
from ring import util

print("Site: add_sightings")
st.header("🔭 Neue Ablesung")

if "new_records" not in st.session_state:
    st.session_state["new_records"] = dict()


place_section(prefill=st.session_state.get("field:place"))
date_section(prefill=util.get_date())


st.button(
    "Neue Ablesung",
    use_container_width=True,
    on_click=sighting_entry,
    kwargs={"gid": len(st.session_state["new_records"]) + 1},
)


for k, group_data in st.session_state["new_records"].items():
    st.markdown(f"**Gruppe {k}**")
    st.button(
        "Weiteren Vogel zu Gruppe Hinzufügen",
        use_container_width=True,
        on_click=sighting_entry,
        kwargs={"gid": k},
        key=f"{k}add",
    )
    util.get_df(group_data)
