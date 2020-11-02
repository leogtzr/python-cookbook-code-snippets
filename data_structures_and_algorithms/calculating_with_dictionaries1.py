prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

# We create two temp variables since the zip function creates an iterator that can be only
# consumed only a single time.
z1 = zip(prices.values(), prices.keys())
z2 = zip(prices.values(), prices.keys())

min_price = min(z1)
max_price = max(z2)

print(min_price)
print(max_price)
