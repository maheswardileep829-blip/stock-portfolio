print("=" * 40)
print("STOCK PORTFOLIO TRACKER")
print("=" * 40)
print()

# Dictionary of stocks you own (stock symbol → number of shares)
portfolio = {
    "AAPL": 2,      # Apple - 10 shares
    "GOOGL": 5,      # Google - 5 shares
    "TSLA": 3,       # Tesla - 3 shares
    "MSFT": 8,       # Microsoft - 8 shares
    "NVDA": 4        # Nvidia - 4 shares
}

# Dictionary of current stock prices (stock symbol → price per share)
prices = {
    "AAPL": 180.50,
    "GOOGL": 140.25,
    "TSLA": 205.00,
    "MSFT": 420.75,
    "NVDA": 875.30
}

# YOUR CODE BELOW THIS LINE:
# ========================================



for stock, shares in portfolio.items():
    
    price = prices[stock]
    value = price * shares
    print (f"{stock}: {shares} shares x  ${price} = ${value}")

total_value = 0
for stock, shares in portfolio.items():
    price = prices[stock]
    value = shares * price
    total_value += value
   
print(f"\nTotal Portfolio Value: ${total_value}")

biggest_stock = ""
biggest_value = 0

for stock, shares in portfolio.items():
    price = prices[stock]
    value = shares * price
    if value > biggest_value:
        biggest_value = value
        biggest_stock = stock
print (f"Biggest holding = ${biggest_value} -- {biggest_stock}")

print ("\n Portfolio Breakdown:")
print ("-" * 30)

for stock, shares in portfolio.items():
    price = prices[stock]
    value = shares * price
    percentage = (value / total_value) * 100
    print (f"{stock} -- {shares}, price = ${round(value, 1)}, percentage of total portfolio = {round(percentage, 1)}%")




# TASK 1: Calculate and print value of each stock
# Loop through portfolio
# For each stock: calculate shares × price
# Print: "AAPL: 10 shares × $180.50 = $1,805.00"


# TASK 2: Calculate total portfolio value
# Add up all the individual stock values
# Print: "Total Portfolio Value: $XXXXX"


# TASK 3: Find your biggest holding
# Which stock is worth the most money?
# Print: "Biggest holding: XXXX ($XXXX)"


# TASK 4: Calculate what percentage each stock is
# Print each stock with its percentage of total portfolio
## **WHAT YOUR OUTPUT SHOULD LOOK LIKE:**
