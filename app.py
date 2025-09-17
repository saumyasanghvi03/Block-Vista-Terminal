import streamlit as st

# All panel imports
from panels.indices_panel import show_indices_panel
from panels.watchlist_panel import show_watchlist_panel
from panels.gainers_losers_panel import show_gainers_losers_panel
from panels.chart_panel import show_chart_panel
from panels.orderbook_panel import show_orderbook_panel
from panels.news_sentiment_panel import show_stock_news_sentiment
from panels.optionchain_panel import show_option_chain
from panels.heatmap_panel import show_market_heatmap
from panels.positions_panel import show_positions_panel
from panels.alerts_panel import show_alerts_panel
from panels.trade_diary_panel import show_diary_panel
from order_placement import show_order_form

st.set_page_config(layout="wide", page_title="BlockVista Terminal")

st.markdown("# BlockVista Terminal : Bloomberg for Indian Stock Traders 🚀")
st.markdown("##### Modular Trading Dashboard using KiteConnect and Streaming APIs")

# Main Panels
col1, col2, col3 = st.columns(3)
bcol1, bcol2, bcol3 = st.columns(3)
with col1: show_indices_panel()
with col2: show_watchlist_panel()
with col3: show_gainers_losers_panel()
with bcol1: show_chart_panel()
with bcol2: show_orderbook_panel()
with bcol3: show_stock_news_sentiment()

st.markdown("## Pro Tools & Insights")
tcol1, tcol2, tcol3 = st.columns(3)
with tcol1: show_market_heatmap()
with tcol2: show_option_chain("NIFTY")
with tcol3: show_positions_panel()
st.sidebar.header("Trading Tools")
show_order_form()
show_alerts_panel()
show_diary_panel()

# ———
# Placeholders for each imported panel: put demo logic in each panel (see prior responses).
# Use st.dataframe/sample data first, then add real API code.
