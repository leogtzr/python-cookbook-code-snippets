import re

url = 'http://www.python.org'
# url = 'alv'

has_schema = re.match('http:|https:|ftp:', url)

if has_schema:
    print('Exist ... ')
