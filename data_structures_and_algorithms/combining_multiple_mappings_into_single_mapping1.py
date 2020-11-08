from collections import ChainMap

# A ChainMap takes multiple mappings and makes them logically appear as one.

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

c = ChainMap(a, b)

for k, v in c.items():
    print(c[k])

print('~~~~~~~~~~~~')

print(c['x'])
print(c['y'])
print(c['z'])

print('~~~~~~~~~~~~~~~~~~~~>')

for k in c.keys():
    print(k)


c['_'] = 'Leonardo'

print(c)

# Mutate an element:
c['z'] = 7456

print(c['z'])

# Removing an element:
del c['x']

print(c)
