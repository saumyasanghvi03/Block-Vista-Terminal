import streamlit as st
import plotly.graph_objs as go
from kiteconnect_api import get_candlestick

def show_chart_panel():
    st.subheader("Candlestick Chart (RELIANCE Demo)")
    df = get_candlestick("RELIANCE")
    if not df.empty:
        fig = go.Figure(data=[go.Candlestick(
            x=df['date'], open=df['open'], high=df['high'], low=df['low'], close=df['close']
        )])
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No data available for candlestick chart.")
