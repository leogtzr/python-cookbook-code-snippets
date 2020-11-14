import re

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

new_text = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\2-\1', text)

print(new_text)
