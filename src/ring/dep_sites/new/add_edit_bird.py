import streamlit as st
from ring.models import Species, Bird
from ring.sites.new.find_bird import find_bird
from ring.fields import Field
from ring.sites.new.save_bird import save_bird

print("Running APP")
st.header("🦢 Vogel anlegen oder bearbeiten")

st.header("Suchmaske")
st.text_input("Ringnummer", key="reading", placeholder="...1234")
st.button("Vogel Finden", on_click=find_bird, use_container_width=True)
st.divider()

selected_bird = st.session_state.get(Field.SELECTED_BIRD.value)
if not selected_bird:
    selected_bird = Bird(id="")

# RING
ring_num = st.text_input("Ringnummer", key=Field.RING_NUM.value, placeholder="...1234")

# SPECIES
species = st.selectbox(
    "Art",
    key=Field.SPECIES.value,
    placeholder="Art",
    options=[s.name for s in Species.all()],
)

# PARTNER
partner = st.text_input("Partner", key=Field.PARTNER.value, placeholder="Ringnummer")

# GENDER
gender = st.selectbox(
    "Geschlecht", key=Field.GENDER.value, options=[None, "M", "W"], index=0
)

# Save
save_btn = st.button("Speichern", key="save_bird_btn", on_click=save_bird)
