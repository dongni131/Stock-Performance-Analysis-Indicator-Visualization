from utils_li import download_stock_data, clean_and_reshape_data, calculate_up_days, calculate_realized_gain_loss, calculate_moving_average, plot_stock_data

def interactive_stock_analyzer():
    """
    Interactive stock analysis tool that allows the user to provide input for:
    - Stock ticker to analyze
    - Date range (start and end dates)
    - A metric to analyze (e.g., up days, realized gain/loss, 20-day moving average)
    Optionally, the user can choose to plot the data.
    The tool will continue to allow analysis of multiple stocks until the user enters 'quit'.
    """
    while True:
        # Get user input for ticker
        ticker = input("Enter the stock ticker (e.g., META or 'quit' to exit): ")
        if ticker.lower() == 'quit':
            break
        
        # Get date range input
        start_date = input("Enter the start date (YYYY-MM-DD): ")
        end_date = input("Enter the end date (YYYY-MM-DD): ")
        
        # Download the stock data
        stock_data = download_stock_data(ticker, start_date, end_date)
        if stock_data is None:
            print("Failed to download data. Please check the ticker or date format.")
            continue
        
        # Clean and reshape the data
        cleaned_data = clean_and_reshape_data(stock_data, ticker)
        if cleaned_data is None:
            print(f"No data available for {ticker} after cleaning.")
            continue
        
        # Ask the user to select a metric for analysis
        print("Select a metric to analyze:")
        print("1. Up days")
        print("2. Realized gain/loss")
        print("3. 20-Day Moving Average")
        metric_choice = input("Enter the number corresponding to your choice (1, 2, or 3): ")
        
        if metric_choice == '1':
            # Calculate and display the number of up days
            up_days = calculate_up_days(cleaned_data)
            print(f"Up Days: {up_days}")
        elif metric_choice == '2':
            # Calculate and display the realized gain/loss
            realized_gain_loss = calculate_realized_gain_loss(cleaned_data)
            print(f"Realized Gain/Loss: {realized_gain_loss}")
        elif metric_choice == '3':
            # Calculate and display the 20-day moving average
            moving_avg = calculate_moving_average(cleaned_data)
            if moving_avg is not None:
                print(f"20-Day Moving Average: {moving_avg.iloc[-1]}")
            else:
                print("Unable to calculate the 20-Day Moving Average.")
        else:
            print("Unrecognized metric choice. Please enter 1, 2, or 3.")
            continue
        
        # Ask if the user wants to plot the data
        plot_option = input("Do you want to plot the stock data? (yes/no): ")
        if plot_option.lower() == 'yes':
            plot_stock_data(cleaned_data, ticker)

if __name__ == "__main__":
    interactive_stock_analyzer()
