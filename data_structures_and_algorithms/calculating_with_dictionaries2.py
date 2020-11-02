prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

min_price_key = min(prices, key=lambda k: prices[k])
max_price_key = max(prices, key=lambda k: prices[k])
#print(min_price_key)

min_price_value = prices[min_price_key]
max_price_value = prices[max_price_key]

print(min_price_value)
print(max_price_value)
