import re
from calendar import month_abbr


def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '[{}] ({}) |{}|'.format(m.group(2), mon_name, m.group(3))


datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

# a substitution callback function
print(datepat.sub(change_date, text))

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# print(month_abbr[12])

for month_num in range(1, 13):
    print(month_abbr[month_num])
