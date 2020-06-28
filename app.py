import yfinance as yf
import matplotlib.pyplot as plt
import datetime
import pandas as pd


#Symbol = 'SPY AMZN TSLA'
selected_symbol = input("Please input stock symbols, i.e. 'SPY AMZN TSLA' : " )


#StockData = yf.Tickers(Symbol)
StockData = yf.Tickers(selected_symbol)
#today = datetime.datetime.today().isoformat()[:10]

while True:
    startdate = input("Please enter the start date in this format '2001-1-1' : " )
    enddate = input("Please enter the end date in this format '2001-1-1' : " )
    StockPrices = StockData.history(period='1d', start=startdate, end=enddate)
    ClosePrices = StockPrices['Close']
    if str(ClosePrices.isnull().values.any()) == "True":
        print("Sorry, please enter a proper time range for the selected stock symbols")
    else:
        break

#StockPrices = StockData.history(period='1d', start='2010-1-1', end='2020-2-10')
#StockPrices = StockData.history(period='1d', start=startdate, end=today)

#print(type(StockPrices['Close'].head()))





stock_return = ClosePrices.apply(lambda x: x / x[0])
#print(stock_return.head())



#StockPrices['Close'].plot(grid=True)
stock_return.plot(grid = True).axhline(y = 1, color = "black", lw = 2)


#plt.show(block=False)


plt.show()
