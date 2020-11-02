from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d['a'])

print(d)# d = defaultdict(set)
# d['a'].add(1)

