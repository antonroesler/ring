LOCATION = "/Users/anton/Projects/ring/data"
FILE = "latest.pkl"
BACKUP = "latest.backup.pkl"
import pathlib
import pickle
import time
from ring.models.bird import Sighting
import streamlit as st


def save_state():
    print("saving state")
    file = pathlib.Path(LOCATION) / FILE
    if "data" in st.session_state:
        if file.exists() and file.is_file():
            file.rename(f"{LOCATION}/{BACKUP}")
        pickle.dump(st.session_state["data"], (pathlib.Path(LOCATION) / FILE).open("wb+"))
    else:
        print("No Data")


