# This is a sample code for calculating RSI and MACD indicators.
import numpy as np
import pandas as pd

def calculate_rsi(data, periods=14):
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=periods).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=periods).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_macd(data, slow=26, fast=12, signal=9):
    exp1 = data.ewm(span=fast, adjust=False).mean()
    exp2 = data.ewm(span=slow, adjust=False).mean()
    macd = exp1 - exp2
    signal_line = macd.ewm(span=signal, adjust=False).mean()
    return macd, signal_line

# Example usage
data = pd.Series([100, 102, 101, 105, 104, 107, 108, 110])
rsi = calculate_rsi(data)
macd, signal = calculate_macd(data)
print("RSI:", rsi)
print("MACD:", macd, "Signal:", signal)
