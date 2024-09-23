import streamlit as st
import math
import random
from ring.sites.data.cache import get_individuals, get_sightings, get_places

st.write("🔎 Datenanalyse")

tab1, tab2, tab3, tab4 = st.tabs(["Bsp. 1", "Bsp. 2", "Bsp. 3", "Orte"])

with tab1:
    st.write("Arten und Anzahl")
    data = get_individuals()
    print(data.head())
    data = data.groupby("Art").count().drop(columns=["Ringnummer"])
    print(data.head())
    st.bar_chart(data)

with tab2:
    st.write("Freundeskreis")
    ring_num = st.text_input("Ringnummer", key="search")
    btn = st.button("Suchen", key="search_btn")

    df = get_sightings()

    # List all dates AND places where the bird was sighted
    if btn:
        df_search_bird = df[df["Ringnummer"].str.contains(ring_num, na=False)]
        list_dates = df_search_bird[["Datum", "Ort"]].drop_duplicates()

        # Now find all birds that were sighted in the same place on the same date
        df_same_date = df[
            df["Datum"].isin(list_dates["Datum"]) & df["Ort"].isin(list_dates["Ort"])
        ]
        # Each bird is counted only once, Create a df with col, Art, Ringnummer, Anzahl
        df_same_date = df_same_date.groupby(["Art", "Ringnummer"]).count().reset_index()
        df_same_date = df_same_date.rename(columns={"Datum": "Anzahl"})
        # Sort by Anzahl
        df_same_date = df_same_date.sort_values(
            by="Anzahl", ascending=False
        ).reset_index()
        st.dataframe(df_same_date[["Art", "Ringnummer", "Anzahl"]])

with tab3:
    # For the top 10 places, count the number of Art that were sighted
    st.write("Top 10 Orte")
    df = get_sightings()
    df = df[df["Ort"].isin(df["Ort"].value_counts().head(10).index)]
    df = df[["Art", "Ort", "Datum"]]
    df = df.groupby(["Ort", "Art"]).count().reset_index().set_index("Ort")
    df = df.sort_values(by=df.columns[0], ascending=False)
    # Create one column for each Art
    df = df.pivot(columns="Art", values="Datum").fillna(0)
    st.bar_chart(df)

with tab4:
    ring_num = st.text_input("Ringnummer", key="search_ort_ring")
    btn = st.button("Suchen", key="search_btn_ort_ring")
    if btn:
        places = get_places()
        df = get_sightings()
        if len(ring_num) > 0:
            st.write(f"Suche nach {ring_num}")
            df = df[df["Ringnummer"].str.contains(ring_num, na=False)]

        max_jitter = 0.002

        def get_lat_lon(row):
            """Adds circular jitter to lat and lon"""
            place = row["Ort"]
            if places[place].lon and places[place].lat:
                angle = random.uniform(0, 2 * 3.1415)
                jitter = random.uniform(0, max_jitter)
                row["lon"] = places[place].lon + jitter * math.cos(angle)
                row["lat"] = places[place].lat + jitter * math.sin(angle)
            else:
                row["lon"] = None
                row["lat"] = None
            return row

        # For each sighting, add the lat and lon to the df
        try:
            df = df.apply(get_lat_lon, axis=1)
            df = df.dropna(subset=["lat", "lon"])

            st.map(df, color=(255, 0, 0, 0.1), use_container_width=True)
        except KeyError:
            st.write("Keine Vollständigen Daten gefunden")
            pass
