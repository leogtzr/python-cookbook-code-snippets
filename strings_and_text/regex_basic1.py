import re

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

if re.match(r'\d+/\d+/\d+', text1):
    print('Yes')
else:
    print('No')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>')
print(re.match(r'\d+/\d+/\d+', text1))
print(re.match(r'\d+/\d+/\d+', text2))
