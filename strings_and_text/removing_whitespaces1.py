import re

s = '  hello       world   \n'

s_result = re.sub('\s+', ' ', s)
print(s_result)
