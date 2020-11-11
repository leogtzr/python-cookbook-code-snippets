import re

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

m = datepat.match('11/27/2020')

if m:
    print('Found...')
    print(m.groups())
    date_tokens = m.groups()
    for dt in date_tokens:
        print(dt)
