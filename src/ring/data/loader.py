LOCATION = "/Users/anton/Projects/ring/data"
FILE = "latest.pkl"
import pathlib
import pickle
import time
from ring.models.bird import Sighting


def load_data() -> list[Sighting]:
    file = pathlib.Path(LOCATION) / FILE
    if file.exists() and file.is_file():
        return pickle.load(file.open("rb"))
    else:
        print("No Data")
