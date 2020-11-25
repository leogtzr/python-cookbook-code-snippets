import re

text = '''
/*
My value

Abc

OK
1

Holis
*/
'''

# In this pattern, (?:.|\n) specifies a noncapture group (i.e., it defines a
# group for the purposes of matching, but that group is not captured separately or numbered).
comment_pattern = re.compile(r'/\*((?:.|\n)*?)\*/')
comment_pattern2 = re.compile(r'/\*(.*?)\*/', re.DOTALL)

for f in comment_pattern.findall(text):
    print(f)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

for f in comment_pattern2.findall(text):
    print(f)
