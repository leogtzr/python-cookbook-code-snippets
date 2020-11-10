from fnmatch import fnmatch, fnmatchcase
import os

filenames = os.listdir('/tmp')

# for file in filenames:
#     print(file)

log_files = [name for name in filenames if fnmatchcase(name, '*.log')]

for file in log_files:
    print(file)
