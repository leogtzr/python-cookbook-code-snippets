from collections import defaultdict

d = defaultdict(list)
pairs = [
    (1, 2),
    (2, 4),
    (3, 8),
    (4, 16)
]

for key, value in pairs:
    d[key].append(value)

print(d)
