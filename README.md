# Stock Portfolio Tracker

A Python program that tracks a stock portfolio and calculates total value, biggest holdings, and percentage breakdown using dictionaries.

## Features

- Track multiple stock holdings with share counts
- Real-time value calculation based on current prices
- Identify biggest portfolio holding
- Calculate percentage breakdown of entire portfolio
- Clean, formatted output

## What It Does

The program:
1. Takes a portfolio of stocks (symbol → shares owned)
2. Takes current stock prices (symbol → price per share)
3. Calculates the value of each holding
4. Finds the total portfolio value
5. Identifies the biggest holding
6. Shows what percentage each stock represents

## Example Output
```
========================================
STOCK PORTFOLIO TRACKER
========================================
AAPL: 2 shares x $180.5 = $361.0
GOOGL: 5 shares x $140.25 = $701.25
TSLA: 3 shares x $205.0 = $615.0
MSFT: 8 shares x $420.75 = $3366.0
NVDA: 4 shares x $875.3 = $3501.2
Total Portfolio Value: $8544.45
Biggest holding = $3501.2 -- NVDA
Portfolio Breakdown:
------------------------------
AAPL: 4.2%
GOOGL: 8.2%
TSLA: 7.2%
MSFT: 39.4%
NVDA: 41.0%
```

## What I Learned

This project helped me practice:
- **Dictionaries**: Storing and accessing key-value pairs
- **Looping through dictionaries**: Using `.items()` to get keys and values
- **Cross-referencing dictionaries**: Using one dictionary's keys to look up values in another
- **Tracking maximum values**: Finding the biggest item while looping
- **Percentage calculations**: Converting values to percentages
- **Debugging**: Fixed multiple bugs with indentation and variable scope

## Technical Details

**Concepts used:**
- Dictionary creation and manipulation
- For loops with `.items()`
- Conditional statements (if/elif/else)
- Mathematical operations
- String formatting with f-strings
- Variable scope and tracking

## Built With

- Python 3.14.2
- Standard library only (no external dependencies)

## Future Improvements

- [ ] Add user input to customize portfolio
- [ ] Pull real-time stock prices from API
- [ ] Save portfolio to file
- [ ] Track portfolio changes over time
- [ ] Add buy/sell transaction functionality
- [ ] Calculate gains/losses

## Author

Built while learning Python dictionaries - February 2026

Part of my journey learning Python and building AI-powered tools for economic analysis.

---

**Project #5** in my Python learning path.
