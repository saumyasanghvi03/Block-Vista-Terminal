import streamlit as st
from kiteconnect_api import kite

def show_orderbook_panel():
    st.subheader("Order Book (Live)")
    orders = kite.orders()
    st.dataframe(orders)
