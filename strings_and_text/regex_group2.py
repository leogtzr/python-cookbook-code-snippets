import re

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

m = datepat.match('11/27/2012')

if m:
    for g in m.groups():
        print(g)
