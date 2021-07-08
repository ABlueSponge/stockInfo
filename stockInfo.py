import yfinance as yf
stonk = input("Enter a stock: ")
stock = yf.Ticker(stonk)
va = stock.info
print(stonk.center(20, "="))
print("Stock Price $"+(str(va["regularMarketPrice"])))
print("52 Week Low: $" + (str(va["fiftyTwoWeekLow"])))
print("52 Week High: $" + (str(va["fiftyTwoWeekHigh"])))
print("50 Day Average: $" + (str(va["fiftyDayAverage"])))
print("Industry: "+(str(va["industry"])))
print("Country: " + (str(va["country"])))
print("Number of Full Time Employees: " + (str(va["fullTimeEmployees"])))
#test
