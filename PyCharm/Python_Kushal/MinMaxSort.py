stocks = {
    'GOOG': 520.45,
    'FB': 76.45,
    'YHOO': 39.28,
    'AAPL': 99.76
}
# you cannot sort the dictionary but can sort zip's first column
zip(stocks.values(), stocks.keys())
print(min(zip(stocks.values(), stocks.keys())))
print(max(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.values(), stocks.keys())))

print("----------------------------------------------------")

print(min(zip(stocks.keys(), stocks.values())))
print(max(zip(stocks.keys(), stocks.values())))
print(sorted(zip(stocks.keys(), stocks.values())))