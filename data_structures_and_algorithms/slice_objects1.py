items = [0, 1, 2, 3, 4, 5, 6]
print(items)

a = slice(2, 4)

print(items[a])
print(items[2:4])

# We can also modify specific slice indexes with the slice object we just created.
items[a] = [2**3, 2**4]

print(items)

print('Removing elements :')
del items[a]

print(items)

print('Getting information from the slice:')
print(a.start)
print(a.stop)
