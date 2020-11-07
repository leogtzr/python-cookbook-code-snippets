import math

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

for n in [math.sqrt(n) for n in mylist if n > 0]:
	print(n)