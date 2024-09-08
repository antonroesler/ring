import streamlit as st
from ring.db import Birds, Bird


@st.dialog("Vorschlag finden 🐦")
def find_bird():
    reading = st.session_state["reading"]

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
                st.session_state["selected_bird"] = bird
                st.session_state["ringnum"] = bird.id
                st.session_state["find_species"] = bird.species
                st.rerun()


if __name__ == "__main__":
    ...
