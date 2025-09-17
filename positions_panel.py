import streamlit as st
from kiteconnect_api import kite

def show_positions_panel():
    st.subheader("My Live Positions")
    pos = kite.positions()
    st.dataframe(pos['net'])  # Show day/net positions live
