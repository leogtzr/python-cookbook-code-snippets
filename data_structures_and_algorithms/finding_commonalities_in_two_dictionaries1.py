a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

print('Keys in common: ')
print(a.keys() & b.keys())

print('Keys in a that are not in b')
print(a.keys() - b.keys())

print('(key,value) pairs in common')
print(a.items() & b.items())

print('Make a new dictionary with certain keys removed:')
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)
