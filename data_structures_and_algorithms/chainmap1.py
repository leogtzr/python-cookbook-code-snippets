from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

c = ChainMap(a, b)

c['z'] = 10
c['w'] = 40

print(c)
