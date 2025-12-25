# Stock Performance Analysis & Indicator Visualization

## Overview

This project performs a financial analysis of selected stocks using historical price data.  
The goal is to compute common performance metrics, visualize price trends, and compare behavior across stocks using simple technical indicators.

The project focuses on **descriptive analysis and visualization**, rather than predictive modeling.

---

## Data Source

- Stock price data is retrieved using the **yfinance** Python package.
- Assets analyzed include:
  - TSLA (Tesla)
  - GOOGL (Alphabet)
- Time period: **Year 2024** (configurable)

---

## Analysis Workflow

The analysis follows these steps:

1. **Data Download**
   - Download daily stock price data (Open, High, Low, Close, Volume).

2. **Data Cleaning & Reshaping**
   - Ensure consistent date formats.
   - Handle missing values.
   - Compute daily returns.

3. **Metric Calculation**
   - **Up Days**: Number of days where Close > Open.
   - **Realized Gain/Loss**: Net price change over the selected period.
   - **20-Day Moving Average**: Trend indicator based on closing prices.

4. **Visualization**
   - Closing price vs. 20-day moving average.
   - Daily return comparison across stocks.
   - Visual comparison of volatility and trends.

---

## Key Metrics

| Metric | Description |
|------|------------|
| Up Days | Number of days with positive daily price movement |
| Daily Return | Percentage change in closing price |
| Realized Gain/Loss | Net gain or loss over the analysis period |
| 20-Day Moving Average | Short-term trend indicator |

---

## Interactive Stock Analyzer

This project includes an **interactive command-line tool** that allows users to:

- Select a stock ticker
- Specify a date range
- Choose a metric to analyze
- Optionally generate plots

The tool runs in a loop until the user exits.

---

## Key Findings

- TSLA showed **higher volatility** but a **larger realized gain**.
- GOOGL demonstrated **more consistent upward movement**.
- Moving averages helped highlight trend differences between assets.

---

## Technologies Used

- Python
- pandas
- numpy
- matplotlib
- yfinance

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
