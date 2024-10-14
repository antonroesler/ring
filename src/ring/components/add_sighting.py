import streamlit as st
import pandas as pd

from ring.components.edit_sighting import form 
def _get_df(gid):
    if gid in st.session_state["new_records"]:
        return st.session_state["new_records"][gid]
    return None


@st.dialog("Neue Ablesung Eingeben", width="large")
def sighting_entry(gid):

    form()
    

            # df: pd.DataFrame =_get_df(gid)
            # if df is not None:
            #     df.loc[len(df)] = new_row.values()
            # else: 
            #     print(new_row.keys())
            #     df = pd.DataFrame(columns=list(new_row.keys()), data=[new_row.values()])
            # st.session_state["new_records"][gid] = df
            # st.rerun(scope="app")