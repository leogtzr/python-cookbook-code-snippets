# Discarding specific value:

a, _, c = 'Leo'         # 'e' will be ignored.

print(a, c)

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
_, shares, price, _ = data

print(shares)
print(price)
