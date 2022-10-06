from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Young Trader indo apps!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


st.write(1234)
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 2000, 3000, 40000],
}))


apikey = 'K8AF2wV5T0z1Pi6YHFFiOvLPnY5MdAKtjIN8AfRfTEFCXzsF8nxC38vwyD6yTkeV'
secret = 'Aryomadan123'
!pip install python-binance pandas mplfinance

#Import library
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import pandas as pd

client = Client(apikey, secret)
tickers = client.get_all_tickers()

ticker_df = pd.DataFrame(tickers)

ticker_df_symbol = ticker_df.drop(columns='price', axis=1)
ticker_df_symbol

historical = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1DAY, '1 Jan 2011')
hist_df_LIT = pd.DataFrame(historical)
hist_df_LIT.columns = ['Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close Time', 'Quote Asset Volume', 
                    'Number of Trades', 'TB Base Volume', 'TB Quote Volume', 'Ignore']

hist_df_LIT['Open Time'] = pd.to_datetime(hist_df_LIT['Open Time']/1000, unit='s')

hist_df_LIT.rename(columns = {"Open Time":"Date"}, inplace=True)
hist_df_LIT.rename(columns = {"Open Time":"Date"}, inplace=True)
hist_df_LIT = hist_df_LIT.set_index('Date')
#hist_df_LIT = hist_df_LIT[['Close']]

#hist_df_LIT.drop(columns='Unnamed: 0', inplace=True)
hist_df_LIT.drop(columns='Ignore', inplace=True)
#hist_df_LIT.rename(columns = {'Close':'Close_LIT'}, inplace=True)
hist_df_LIT = hist_df_LIT
hist_df_LIT
