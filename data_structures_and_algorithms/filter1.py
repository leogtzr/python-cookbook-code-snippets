def is_int(val):
	try:
		x = int(val)
		return True
	except ValueError:
		return False

values = ['1', '2', '-3', '-', '4', 'N/A', '5']

# print(type(filter(is_int, values)))

i_vals = list(filter(is_int, values))
print(i_vals)