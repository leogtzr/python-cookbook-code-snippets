import re

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

datepat = re.compile(r'\d+/\d+/\d+')

for dt in datepat.findall(text):
    print(dt)
