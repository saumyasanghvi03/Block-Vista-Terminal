# BlockVista Terminal

A Bloomberg-style advanced Indian Stock Market terminal for traders and investors—built with Streamlit and KiteConnect APIs. 

## Key Features

- 6 split-panel live dashboard
- Realtime indices, watchlist, gainers/losers, candlestick charts
- F&O option chain and volumetric heatmap
- Position & P&L tracker, live order book
- Stock-specific news & X/Twitter sentiment feeds
- Place and track orders (KiteConnect)
- ML-powered custom screeners
- Price alerts and trade diary with notes

## Directory

- `streamlit_app.py` — Main Streamlit dashboard app
- `requirements.txt` — All dependencies
- `panels/` — Modular UI code for each dashboard panel
- `.gitignore` — Exclude creds and Python cache

## Setup

1. Clone the repo
2. Install with `pip install -r requirements.txt`
3. Add your Kite credentials via `.env` or config
4. Run `streamlit run streamlit_app.py`

---

*For live API, custom alerts, and sentiment: fill in panel logic as per your strategy!*
