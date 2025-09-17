import streamlit as st
from kiteconnect_api import get_watchlist_live

def show_watchlist_panel():
    symbols = st.text_input("Your Watchlist (comma-separated)", "RELIANCE,HDFCBANK,TATAMOTORS").split(",")
    st.dataframe(get_watchlist_live([s.strip() for s in symbols if s.strip()]))
