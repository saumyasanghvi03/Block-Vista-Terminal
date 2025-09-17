import streamlit as st
import feedparser

def show_stock_news_sentiment(symbol="RELIANCE"):
    st.subheader(f"Live News & Sentiment - {symbol}")
    feed = feedparser.parse(f"https://news.google.com/rss/search?q={symbol}+stock")
    for entry in feed.entries[:5]:
        st.write(f"🟢 {entry.title} | {entry.source.title if 'source' in entry else ''}")
