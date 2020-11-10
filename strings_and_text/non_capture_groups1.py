import re

line = 'asdf fjdk; afed, fjek,asdf,      foo'

tokens = re.split(r'(?:,|;|\s)\s*', line)

for token in tokens:
    print(token)
