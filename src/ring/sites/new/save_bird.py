import streamlit as st
from ring.db import Birds, Bird
from ring.fields import Field


@st.dialog("Vogel Speichern  🐦")
def save_bird():
    st.write(f"Ringnummer: {st.session_state.get(Field.RING_NUM.value)}")
    bird = Bird(id=st.session_state.get(Field.RING_NUM.value))
    if existing := Birds.get(st.session_state.get(Field.RING_NUM.value)):
        existing: Bird
        st.write("Folgende Werte werden überschrieben:")
        if existing.species != st.session_state.get(Field.SPECIES.value):
            st.write(
                f"❗️ Art: {existing.species} → {st.session_state.get(Field.SPECIES.value)}"
            )
            existing.species = str(st.session_state.get(Field.SPECIES.value)).strip()
        if existing.partner != st.session_state.get(Field.PARTNER.value):
            st.write(
                f"❗️ Partner: {existing.partner} → {st.session_state.get(Field.PARTNER.value)}"
            )
            existing.partner = str(st.session_state.get(Field.PARTNER.value)).strip()
        if existing.gender != st.session_state.get(Field.GENDER.value):
            st.write(
                f"❗️ Geschlecht: {existing.gender} → {st.session_state.get(Field.GENDER.value)}"
            )
            existing.gender = str(st.session_state.get(Field.GENDER.value)).strip()
        bird = existing

    else:
        st.write("Folgende Werte werden gespeichert:")
        st.write(f"Art: {st.session_state.get(Field.SPECIES.value)}")
        st.write(f"Partner: {st.session_state.get(Field.PARTNER.value)}")
        st.write(f"Geschlecht: {st.session_state.get(Field.GENDER.value)}")
        bird.species = str(st.session_state.get(Field.SPECIES.value)).strip()
        bird.partner = str(st.session_state.get(Field.PARTNER.value)).strip()
        bird.gender = str(st.session_state.get(Field.GENDER.value)).strip()

    col1, col2 = st.columns(2)
    with col1:
        save = st.button("Speichern", key="save_btn")
    with col2:
        stop = st.button("Abbrechen", key="cancel_btn")
    if save:
        Birds.upsert(bird)
        st.rerun()
    if stop:
        st.rerun()
