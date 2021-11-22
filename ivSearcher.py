import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib as mp
import mibian as mb
import scipy

print("Enter desired IV: ")
ivr = float(input())

table = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

df = table[0]

symbols = df['Symbol']
spx = symbols.to_numpy()
for equity in spx:
    stock = yf.Ticker(equity)
    price = stock.info["regularMarketPrice"]
    strike = price + 5
    ir = 0
    dte = 5

    callprice = 100

    call = mb.BS([price, strike, ir, dte], callPrice = callprice)
    currentIV = call.impliedVolatility

    if (currentIV >= ivr):
        print(str(equity) + " - $" + str(price) + "(" + str(currentIV) + ")")