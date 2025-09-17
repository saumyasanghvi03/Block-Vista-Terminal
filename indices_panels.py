import streamlit as st
from kiteconnect_api import get_indices_live

def show_indices_panel():
    st.subheader("Live Indices")
    st.dataframe(get_indices_live())
