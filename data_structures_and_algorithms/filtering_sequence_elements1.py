mylist = [1, 4, -5, 10, -7, 2, 3, -1]
for n in [n for n in mylist if n > 0]:
	print(n)

for n in [n for n in mylist if n < 0]:
	print(n)

# Using a generator expression:

print('~~~~~~~~~~~~~~~~~>')

pos = (n for n in mylist if n > 0)
for x in pos:
	print(x)
