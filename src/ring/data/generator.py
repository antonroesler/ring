LOCATION = "/Users/anton/Projects/ring/data"
FILE = "latest.pkl"
import pathlib
import pickle
import time
import streamlit as st
from ring.components.add_sighting import sighting_entry
import pandas as pd
from ring.models.bird import Sighting
import random
import string
import numbers
from datetime import datetime
from ring.data.loader import load_data


data = [
    Sighting(
        reading="H29384A",
        ring="H29384A",
        species="Graugans",
        place="Ostpark",
        Datum=datetime(year=2024, month=2, day=27, hour=15),
    ),
    Sighting(
        reading="...9384A",
        ring="H29384A",
        species="Graugans",
        place="Ostpark",
        Datum=datetime(year=2024, month=2, day=27, hour=15),
    ),
    Sighting(
        reading="H29384A",
        ring="H29384A",
        species="Graugans",
        place="Hafenpark",
        Datum=datetime(year=2024, month=3, day=4, hour=15),
    ),
    Sighting(
        reading="129991",
        ring="129991",
        species="Kanadagans",
        place="Hafenpark",
        Datum=datetime(year=2024, month=3, day=5, hour=15),
    ),
    Sighting(
        reading="...9992",
        ring="129991",
        species="Kanadagans",
        place="Hafenpark",
        Datum=datetime(year=2024, month=3, day=5, hour=15),
    ),
]

for x in range(2):
    r = "".join(random.sample(string.ascii_uppercase + string.digits, k=8))
    data.append(
        Sighting(
            reading=r,
            ring=r,
            place=random.choice(["Ostpark", "Carl-Urlich-Brücke", "Rebstockpark"]),
            Datum=datetime(
                year=2024,
                month=random.randint(1, 10),
                day=random.randint(1, 28),
                hour=random.randint(5, 22),
            ),
        )
    )


s = time.time_ns()
pickle.dump(data, (pathlib.Path(LOCATION) / FILE).open("wb+"))
print(time.time_ns() - s)
