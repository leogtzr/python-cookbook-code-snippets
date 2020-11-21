import re

text = 'Computer says "no." Phone says "yes."'
str_pat = re.compile(r'\"(.*?)\"')

# non-greedy

for match in str_pat.findall(text):
    print(match)
