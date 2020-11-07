from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shres', 'price'])

s = Stock('ACME', 100, 123.45)

print(s)

s = s._replace(shres=89)
print(s)