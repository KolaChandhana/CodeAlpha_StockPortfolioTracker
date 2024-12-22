import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
portfolio = [
    {"ticker": "AAPL", "quantity": 10, "purchase_price": 150},
    {"ticker": "GOOGL", "quantity": 5, "purchase_price": 2800},
    {"ticker": "AMZN", "quantity": 2, "purchase_price": 3400},
]
def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)
    current_price = stock.history(period="1d")["Close"].iloc[-1]
    return current_price
def calculate_portfolio(portfolio):
    data = []
    total_investment = 0
    total_value = 0
    
    for stock in portfolio:
        ticker = stock["ticker"]
        quantity = stock["quantity"]
        purchase_price = stock["purchase_price"]
        current_price = fetch_stock_data(ticker)
        
        investment = quantity * purchase_price
        current_value = quantity * current_price
        profit_loss = current_value - investment
        
        total_investment += investment
        total_value += current_value
        
        data.append({
            "Ticker": ticker,
            "Quantity": quantity,
            "Purchase Price": purchase_price,
            "Current Price": round(current_price, 2),
            "Investment": investment,
            "Current Value": round(current_value, 2),
            "Profit/Loss": round(profit_loss, 2)
        })
    
    return pd.DataFrame(data), total_investment, total_value
df, total_investment, total_value = calculate_portfolio(portfolio)
print("Portfolio Summary")
print(df)
print(f"\nTotal Investment: ${total_investment:.2f}")
print(f"Current Portfolio Value: ${total_value:.2f}")
print(f"Overall Profit/Loss: ${total_value - total_investment:.2f}")
plt.figure(figsize=(10, 6))
plt.bar(df["Ticker"], df["Profit/Loss"], color=["green" if x > 0 else "red" for x in df["Profit/Loss"]])
plt.title("Profit/Loss by Stock")
plt.xlabel("Stock Ticker")
plt.ylabel("Profit/Loss ($)")
plt.axhline(0, color='black', linewidth=0.5)
plt.show()
