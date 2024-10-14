import streamlit as st
from ring.models import Birds, Bird
from ring.fields import Field


@st.dialog("Vorschlag finden 🐦")
def find_bird():
    reading = st.session_state[Field.READING.value]

    if reading is None or len(reading) == 0:
        st.error("Bitte gebe eine Ablesung eingeben")
        return
    birds: list[Bird] = Birds.ring_query(reading)
    print(birds)
    if not birds:
        st.error("Kein Vogel gefunden")
        return
    st.write("Vorschläge:")
    for bird in birds:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write(f"{bird.id}")
        with col2:
            st.write(f"{bird.species}")
        with col3:
            st.write(f"{len(bird.sightings)} Ablesungen")
        with col4:
            btn = st.button("Wählen", key=f"select_{bird.id}")
            if btn:
                st.session_state[Field.SELECTED_BIRD.value] = bird
                st.session_state[Field.RING_NUM.value] = bird.id
                st.session_state[Field.SPECIES.value] = bird.species
                st.session_state[Field.PARTNER.value] = bird.partner
                st.session_state[Field.GENDER.value] = bird.gender
                st.rerun()


if __name__ == "__main__":
    ...
