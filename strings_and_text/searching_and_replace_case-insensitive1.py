import re

text = 'UPPER PYTHON, lower python, Mixed Python'
for m in re.findall('python', text, flags=re.IGNORECASE):
    print(m)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

replace = re.sub('python', 'snake', text, flags=re.IGNORECASE)
'UPPER snake, lower snake, Mixed snake'

print(replace)
