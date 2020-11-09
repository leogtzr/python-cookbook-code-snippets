import re

line = 'asdf fjdk; afed, fjek,asdf,      foo'

# tokens = re.split(r'[;,\s]\s*', line)

# for tok in tokens:
#     print(tok)

fields = re.split(r'(;|,|\s)\s*', line)

# for field in fields:
#     print(field)

# print(fields)

values = fields[::2]
# print(values)

delimiters = fields[1::2] + ['']

# print(delimiters)

joined = ''.join(f"[{v}]+[{d}] " for v, d in zip(values, delimiters))
print(joined)
