import yfinance as yf
import matplotlib.pyplot as plt

def fetch_stock_data(ticker, period="1mo"):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period)
    return hist

def plot_stock_data(hist, ticker):
    plt.figure(figsize=(10, 5))
    plt.plot(hist['Close'], label=f'{ticker} Close Price')
    plt.title(f'{ticker} Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()