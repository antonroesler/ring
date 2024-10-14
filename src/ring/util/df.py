import streamlit as st
import pandas as pd
from ring.models.bird import Sighting


def get_df(data: list[Sighting]):
    return st.dataframe(
        pd.DataFrame(
            data=[obj.model_dump(by_alias=True) for obj in data],
        ),
        selection_mode="single-row",
        on_select="rerun",
        use_container_width=True,
        hide_index=True,
        column_config={"Datum": st.column_config.DateColumn(format="DD.MM.YYYY")},
        column_order=[
            "Ringnummer",
            "Datum",
            "Art",
            "Ort",
            "Ablesung",
            "Farbring",
            "Ablesung (Farbring)",
            "Geschlecht",
            "Alter",
            "Partner",
            "Kleingruppengröße",
            "Gruppengröße",
            "Habitat",
            "Typ",
            "Kommentar",
            "Melder",
            "Gemeldet",
            "Gruppen ID",
        ],
    )