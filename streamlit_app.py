import pandas as pd
import streamlit as st
import numpy as np

import numpy as np
import time as tm
import datetime as dt
import tensorflow as tf

# Data preparation
from yahoo_fin import stock_info as yf
from sklearn.preprocessing import MinMaxScaler
from collections import deque

# AI
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout

# Graphics library
import matplotlib.pyplot as plt

st.title("Welcome to Streamlit!")


# SETTINGS

# Window size or the sequence length, 7 (1 week)
N_STEPS = 7

# Lookup steps, 1 is the next day, 3 = after tomorrow
LOOKUP_STEPS = [1, 2, 3]

# Stock ticker, GOOGL
STOCK = 'FIRE.JK'

# Current date
date_now = tm.strftime('%Y-%m-%d')
date_5_years_back = (dt.date.today() - dt.timedelta(days=1840)).strftime('%Y-%m-%d')


# LOAD DATA 
# from yahoo_fin 
# for 1104 bars with interval = 1d (one day)
init_df = yf.get_data(
    STOCK, 
    start_date=date_5_years_back, 
    end_date=date_now, 
    interval='1d')



st.write("Line Chart in Streamlit")
# 10 * 2 dimensional data

st.line_chart(chart_data)
