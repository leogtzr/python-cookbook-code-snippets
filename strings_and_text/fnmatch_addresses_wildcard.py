from fnmatch import fnmatchcase

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

addresses = [addr for addr in addresses if fnmatchcase(addr, '* ST')]

for a in addresses:
    print(a)
