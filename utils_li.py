import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

def download_stock_data(tickers, start_date, end_date):
    """
    Download stock data for a specified stock code and date range.
    
    parameters:
    tickers (str or list): Individual stock code or list of stock codes
    start_date (str): Start date in 'YYYY-MM-DD' format
    end_date (str): End date in 'YYYY-MM-DD' format
    
    return:
    pd.DataFrame: MultiIndex DataFrame with stock data
    """
    try:
        if isinstance(tickers, str):
            tickers = [tickers]  # If a single ticker symbol is passed in, convert to a list
        
        # Download data
        stock_data = yf.download(tickers, start=start_date, end=end_date, group_by='ticker')
        return stock_data
    except Exception as e:
        print(f"Error downloading data for {tickers}: {e}")
        return None

def clean_and_reshape_data(stock_data, ticker):
    """
    Cleaning and reshaping stock data.
    
    parameters:
    stock_data (pd.DataFrame): MultiIndex DataFrame with stock data
    ticker (str): Ticker Symbol
  
    return:
    pd.DataFrame: Cleansed and reshaped stock data
    """
    if stock_data.empty:
        print(f"Warning: No data found for {ticker}.")
        return None
    
    # Extract current stock data
    ticker_data = stock_data[ticker].copy()
    
    # 1. Check for missing values
    if ticker_data.isnull().any().any():
        print(f"Warning: Missing values found for {ticker}. Filling missing values...")
        ticker_data.fillna(method='ffill', inplace=True)  # Handling missing values with forward padding
    
    # 2. Check for duplicate values
    if ticker_data.duplicated().any():
        print(f"Warning: Duplicate rows found for {ticker}. Removing duplicates...")
        ticker_data.drop_duplicates(inplace=True)
    
    # 3. Add new columns (Daily Up/Down)
    ticker_data['Daily_Return'] = ticker_data['Close'].pct_change()
    
    # 4. Re-indexing
    ticker_data.reset_index(inplace=True)
    
    # 5. Return cleaned data
    return ticker_data

def calculate_up_days(stock_data):
    """
    Calculation of “days up” for a given time frame
    
    parameters:
    stock_data (pd.DataFrame): DataFrame with stock data
    
    return:
    int: Number of days up
    """
    if stock_data.empty:
        print("Warning: No data found.")
        return 0
    
    # Calculate the number of days up
    up_days = (stock_data['Close'] > stock_data['Open']).sum()
    return int(up_days)

def calculate_realized_gain_loss(stock_data):
    """
    Calculate the realized profit and loss for a given time frame.
    
    parameters:
    stock_data (pd.DataFrame): DataFrame with stock data
    
    return:
    float: make a profit and loss
    """
    if stock_data.empty or len(stock_data) < 2:
        print("Warning: Not enough data.")
        return 0.0
    
    # Calculation of realized gains and losses
    initial_price = stock_data['Close'].iloc[0]
    final_price = stock_data['Close'].iloc[-1]
    return final_price - initial_price

def calculate_moving_average(stock_data, window=20):
    """
    Calculates the moving average for a given time window.
    
    parameters:
    stock_data (pd.DataFrame): DataFrame with stock data
    window (int): Moving Average Window Size
    
    return:
    pd.Series: Moving Average Data
    """
    if stock_data.empty:
        print("Warning: No data found.")
        return None
    
    # Calculating Moving Averages
    moving_avg = stock_data['Close'].rolling(window=window).mean()
    return moving_avg

def plot_stock_data(stock_data, ticker):
    """
    Plot a stock's closing price and 20-day moving average.
    
    parameters:
    stock_data (pd.DataFrame): DataFrame with stock data
    ticker (str): Ticker Symbol
    """
    if stock_data.empty:
        print(f"Error: No data to plot for {ticker}.")
        return
    
    # Calculating the 20-day moving average
    moving_avg = calculate_moving_average(stock_data, window=20)
    
    # plot
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Date'], stock_data['Close'], label='Closing Price', color='blue')
    plt.plot(stock_data['Date'], moving_avg, label='20-Day Moving Average', color='orange')
    plt.title(f'{ticker} Stock Price and 20-Day Moving Average')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()


def compare_stock_metrics(stock_data, tickers, metric):
    """
    Compare different stocks for a particular indicator.
    
    parameters:
    stock_data (dict): Dictionary with multiple stock data
    tickers (list): Stock Code List
    metric (str): Metrics to compare
    """
    plt.figure(figsize=(10, 6))
    
    for ticker in tickers:
        if ticker in stock_data:
            plt.plot(stock_data[ticker]['Date'], stock_data[ticker][metric], label=ticker)
    
    plt.title(f'Comparison of {metric} Across Stocks')
    plt.xlabel('Date')
    plt.ylabel(metric)
    plt.legend()
    plt.grid()
    plt.show()
