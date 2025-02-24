from src.agent import create_agent
from src.tools import fetch_stock_data, plot_stock_data

def main():
    assistant, user_proxy = create_agent()
    user_proxy.initiate_chat(assistant, message="Fetch and plot the stock data for AAPL.")

if __name__ == "__main__":
    main()