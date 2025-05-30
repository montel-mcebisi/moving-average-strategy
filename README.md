#  Moving Average Crossover Strategy

This is a simple trading strategy that uses a 10-day and 50-day moving average crossover to generate trading signals on Microsoft stock data. It simulates buying 1 share when the short-term moving average crosses above the long-term average.

## Strategy Logic

- **Buy** 1 share when MA10 > MA50
- **Sell** at the next day's closing price
- Record profit only when a position is taken
- Track total wealth (cumulative profit)

> This is a basic backtest meant for learning — it doesn't include transaction costs or risk management.

---

##  Technologies Used

- Python 
- Pandas 
- Matplotlib 
- Jupyter Notebook (optional)

---

