import re
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext)
print(n)
