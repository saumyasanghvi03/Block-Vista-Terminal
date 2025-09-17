import streamlit as st
from kiteconnect_api import get_watchlist_live

def show_alerts_panel():
    st.subheader("Set Price Alerts (Real)")
    symbol = st.text_input("Symbol for Alert", "RELIANCE")
    alert_price = st.number_input("Target Price", 2500.0)
    check = st.button("Check Now")
    if check:
        ltp = get_watchlist_live([symbol]).iloc[0]['LTP']
        if ltp >= alert_price:
            st.success(f"{symbol} above {alert_price}! LTP: {ltp}")
        else:
            st.write(f"Current price: {ltp}")
