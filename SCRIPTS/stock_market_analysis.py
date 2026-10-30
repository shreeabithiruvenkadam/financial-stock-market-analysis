## Financial Stock Market Analysis in Python
## Analysis of Reliance, TCS, Infosys and HDFC Bank
## Data Source: Yahoo Finance

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import os
##
## Create output folder
os.makedirs("output", exist_ok=True)


print("Libraries imported successfully!")

reliance=yf.download(
    "RELIANCE.NS",
    period="1y",
    interval="1d",
    auto_adjust=True
    )
reliance.head()
reliance.shape
print("Rows:",reliance.shape[0])
print("columns:",reliance.shape[1])
reliance.tail()
print(reliance.columns)
reliance.head()
print(reliance.empty)
reliance.columns
reliance.info()
reliance.isnull().sum()


#### Select stocks

stocks=["RELIANCE.NS","TCS.NS","INFY.NS","HDFCBANK.NS"]

## Download 1 year of daily stock data
data=yf.download(
    stocks,
    period="1y",
    interval="1d",
    auto_adjust=True
    )
print("Stock data downloaded successfully!")
print(data.shape)
print(data.head())
print(data.columns)
print(data.isnull().sum())

data.columns=[
    f"{ticker}_{price}"
    for price,ticker in data.columns
    ]
print(data.head())
print(data.columns.tolist())
print(data.shape)
data.info()
print(data.describe())
print("start Date:",data.index.min())
print("End Date:",data.index.max())
print(data.isnull().sum())


plt.figure(figsize=(12,6))
plt.plot(data.index, data["RELIANCE.NS_Close"], label="Reliance")
plt.plot(data.index, data["TCS.NS_Close"], label="TCS")
plt.plot(data.index, data["INFY.NS_Close"], label="Infosys")
plt.plot(data.index, data["HDFCBANK.NS_Close"], label="HDFC Bank")

plt.title("Stock Price Trend-Last 1 year")
plt.xlabel("Date")
plt.ylabel("Closing price(₹)")
plt.legend()
plt.grid(True)

plt.savefig("price_trend.png")
plt.show()

print(data.columns)
reliance_close=data["RELIANCE.NS_Close"]
print(reliance_close.head())

returns=data[
    [
        "RELIANCE.NS_Close",
        "TCS.NS_Close",
        "INFY.NS_Close",
        "HDFCBANK.NS_Close"
        ]
    ].pct_change()
print(returns.head())

returns.columns=["Reliance","TCS","Infosys","HDFC Bank"]
print(returns.head())

summary=returns.describe().T
print(summary)

performance=returns.agg(
   ["mean","std","min","max"]
    ).T
performance.columns=[
    "Average Daily Return",
    "Volatility",
    "Minimum Return",
    "Maximum Return"
    ]
print(performance)
performance=performance*100
print(performance)

performance=performance.round(3)
print(performance)

performance.sort_values(
    "Average Daily Return",
    ascending=False
    )
volatility=returns.std()*100
print(volatility)

most_volatile=volatility.idxmax()
highest_volatility=volatility.max()
print("most Volatile Stock:",most_volatile)
print("Volatility:",round(highest_volatility,3),"%")

least_volatile=volatility.idxmin()
lowest_volatility=volatility.min()
print("Least Volatile Stock:", least_volatile)
print("Volatility:",round(lowest_volatility,3), "%")

plt.figure(figsize=(10,5))
plt.bar(volatility.index,volatility.values)
plt.title("Volatility Comparison of Stocks")
plt.xlabel("Stock")
plt.ylabel("Volatility (%)")
plt.grid(axis="y")

plt.savefig("output/volatility_comparison.png")
plt.show()

best_stock=performance["Average Daily Return"].idxmax()
best_return=performance["Average Daily Return"].max()
print("Best Performing Stock:", best_stock)
print("Average Daily Return:", round(best_return,3),"%")

worst_stock=performance["Average Daily Return"].idxmin()
worst_return=performance["Average Daily Return"].min()
print("worst Performing Stock:",worst_stock)
print("Average Daily Return:",round(worst_return,3),"%")


cumulative_returns=(1+returns).cumprod()
print(cumulative_returns.tail())

plt.figure(figsize=(12,6))

plt.plot(cumulative_returns.index, cumulative_returns["Reliance"], label="Reliance")
plt.plot(cumulative_returns.index, cumulative_returns["TCS"], label="TCS")
plt.plot(cumulative_returns.index, cumulative_returns["Infosys"], label="Infosys")
plt.plot(cumulative_returns.index, cumulative_returns["HDFC Bank"], label="HDFC Bank")

plt.title("Cumulative Returns of Stocks")
plt.xlabel("Date")
plt.ylabel("Growth of ₹1")
plt.legend()
plt.grid(True)

plt.savefig("output/cumulative_returns.png")
plt.show()


final_cumulative=cumulative_returns.iloc[-1]
print("Final Cumulative Value:")
print(final_cumulative)

total_return=(final_cumulative-1)*100
print("Total Return (%):")
print(total_return.round(2))

highest_total_return_stock = total_return.idxmax()
highest_total_return = total_return.max()

print("Highest Total Return Stock:", highest_total_return_stock)
print("Total Return:", round(highest_total_return, 2), "%")


plt.figure(figsize=(10,5))

plt.bar(total_return.index, total_return.values)

plt.title("Total Return Comparison of Stocks")
plt.xlabel("Stock")
plt.ylabel("Total Return (%)")
plt.grid(axis="y")

plt.savefig("output/total_return_comparison.png")
plt.show()


risk_return = pd.DataFrame({
    "Total Return (%)": total_return,
    "Volatility (%)": volatility
})

risk_return = risk_return.round(2)

print("Risk and Return Comparison:")
print(risk_return)


plt.figure(figsize=(10,6))

plt.scatter(
    risk_return["Volatility (%)"],
    risk_return["Total Return (%)"]
)

for stock in risk_return.index:
    plt.annotate(
        stock,
        (
            risk_return.loc[stock, "Volatility (%)"],
            risk_return.loc[stock, "Total Return (%)"]
        )
    )

plt.title("Risk vs Return of Stocks")
plt.xlabel("Volatility (%)")
plt.ylabel("Total Return (%)")
plt.grid(True)

plt.savefig("output/Risk_vs_Return.png")
plt.show()


final_summary = pd.DataFrame({
    "Average Daily Return (%)": performance["Average Daily Return"],
    "Volatility (%)": performance["Volatility"],
    "Minimum Daily Return (%)": performance["Minimum Return"],
    "Maximum Daily Return (%)": performance["Maximum Return"],
    "Total Return (%)": total_return
})

final_summary = final_summary.round(2)

print("Final Stock Analysis Summary:")
print(final_summary)


final_summary.to_excel("stock_analysis_summary.xlsx")

print("Final summary saved successfully!")


data.to_excel("stock_price_data.xlsx")

print("Stock price data saved successfully!")


ranking = total_return.sort_values(ascending=False)

print("Stock Performance Ranking:")
print(ranking.round(2))


ranking.to_excel("stock_performance_ranking.xlsx")

print("Ranking saved successfully!")


highest_daily_return = returns.max().max()
lowest_daily_return = returns.min().min()

highest_stock = returns.max().idxmax()
lowest_stock = returns.min().idxmin()

print("Highest Daily Return:", round(highest_daily_return * 100, 2), "%")
print("Stock:", highest_stock)

print("Lowest Daily Return:", round(lowest_daily_return * 100, 2), "%")
print("Stock:", lowest_stock)


plt.figure(figsize=(10,6))

plt.hist(returns["Reliance"].dropna(), bins=30, alpha=0.5, label="Reliance")
plt.hist(returns["TCS"].dropna(), bins=30, alpha=0.5, label="TCS")
plt.hist(returns["Infosys"].dropna(), bins=30, alpha=0.5, label="Infosys")
plt.hist(returns["HDFC Bank"].dropna(), bins=30, alpha=0.5, label="HDFC Bank")

plt.title("Daily Return Distribution of Stocks")
plt.xlabel("Daily Return")
plt.ylabel("Number of Days")
plt.legend()
plt.grid(True)

plt.savefig("output/daily_return_distribution.png")
plt.show()








