import os
files = os.listdir('.')
if any(name.endswith('.py') for name in files):
    print('There are python files')
else:
    print('Sorry, no python')
