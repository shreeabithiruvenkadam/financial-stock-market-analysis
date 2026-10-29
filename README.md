Financial Stock Market Analysis in Python



&#x20;1. Project Overview



This project analyzes the stock market performance of four major companies using Python and real stock market data.



The companies analyzed are:



\* Reliance Industries

\* TCS

\* Infosys

\* HDFC Bank



The project focuses on stock prices, daily returns, volatility, cumulative returns, total returns, and risk-return comparison.



&#x20;2. Objectives



The main objectives of this project are:



\* To collect real stock market data using Python

\* To analyze daily stock price movements

\* To calculate daily returns

\* To measure stock volatility

\* To compare total returns

\* To analyze cumulative returns

\* To compare risk and return

\* To visualize stock market performance using charts



&#x20;3. Data Source



The stock market data was collected using the `yfinance` Python library, which retrieves financial market data from Yahoo Finance.



The analysis uses approximately one year of daily stock market data.



&#x20;4. Companies Analyzed



| Company                   | Stock Symbol |

| ------------------------- | ------------ |

| Reliance Industries       | RELIANCE.NS  |

| Tata Consultancy Services | TCS.NS       |

| Infosys                   | INFY.NS      |

| HDFC Bank                 | HDFCBANK.NS  |



&#x20;5. Tools and Technologies



\* Python

\* Pandas

\* NumPy

\* Matplotlib

\* yfinance

\* Microsoft Excel



&#x20;6. Analysis Performed



&#x20;**Stock Price Analysis**



The daily closing prices of the four stocks were analyzed and visualized using line charts.



&#x20;**Daily Return Analysis**



Daily returns were calculated using the percentage change in closing prices.



&#x20;**Volatility Analysis**



Standard deviation of daily returns was used to measure stock price volatility.



Higher volatility indicates larger day-to-day price movements.



&#x20;**Cumulative Return Analysis**



Cumulative returns were calculated to observe how the value of an initial investment changes over the analysis period.



&#x20;**Total Return Analysis**



The total return over the analysis period was calculated for each stock and compared.



&#x20;**Risk and Return Analysis**



Volatility was compared with total return to understand the relationship between risk and return for the selected stocks.



**Daily Return Distribution**



Histograms were used to visualize the distribution of daily returns for each stock.



&#x20;7. Project Outputs



The project generates the following output files:



Excel Files



\* `stock\_price\_data.xlsx` — cleaned stock price data

\* `stock\_analysis\_summary.xlsx` — final analysis summary

\* `stock\_performance\_ranking.xlsx` — stock performance comparison



Charts



\* price\_trend.png

\* volatility\_comparison.png

\* cumulative\_returns.png

\* total\_return\_comparison.png

\* risk\_vs\_return.png

\* daily\_return\_distribution.png



8\. Python Script



The main Python program is:



Stock\_market\_analysis.py



The script downloads the stock data, performs the analysis, creates charts, and saves the results.



9\. Conclusion



This project demonstrates how Python can be used to collect, process, analyze, and visualize financial stock market data.



The analysis provides a comparison of stock price movements, returns, volatility, cumulative performance, and risk-return characteristics of the selected companies.



10\. How to Run the Project



Install the required Python libraries and run:



text

python Stock\_market\_analysis.py



The program will download the stock data and generate the analysis outputs and charts.



11\. Note



Stock market data and results can change over time because financial markets are continuously changing. Therefore, results may differ when the project is executed again at a later date.



