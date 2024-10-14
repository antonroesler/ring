LOCATION = "/Users/anton/Projects/ring/data"
FILE = "latest.pkl"
import pathlib
import pickle
import time
from ring.models.bird import Sighting
import streamlit as st


def load_data() -> list[Sighting]:
    file = pathlib.Path(LOCATION) / FILE
    if file.exists() and file.is_file():
        st.session_state["data"] =  pickle.load(file.open("rb"))
    else:
        print("No Data")