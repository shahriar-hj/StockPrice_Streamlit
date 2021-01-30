import yfinance as yf
import streamlit as st
import pandas as pd

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75      Article

st.write('''
# Simple Stock Price App

show the stock price and volume of the google

''')

# define ticker Symbol
tickerSymbol = "AAPL"
# get data of this ticker
tickerData = yf.Ticker(tickerSymbol)
# Get History of ticker
tickerDf = tickerData.history(period='1y', start='2014-5-31',
                              end='2020-5-31')  # period: the frequency at which to gather the data; common options would include ‘1d’ (daily), ‘1mo’ (monthly), ‘1y’ (yearly)
# See Data
print(tickerDf)
# get stock Information
print(tickerData.info)
# get event data for ticker
print(tickerData.calendar)
# get recommendation data for ticker
print(tickerData.recommendations)

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)