import re

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

for month, day, year in datepat.findall(text):          # Destructuring.
    # print(len(oc))
    print(f"{month}-{day}-{year}")

print('...............')

for m in datepat.finditer(text):
    print(m.groups())
