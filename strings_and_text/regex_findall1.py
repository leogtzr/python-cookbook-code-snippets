import re

# Be aware, though, that if you’re going to perform a lot of matching or searching,
# it usually pays to compile the pattern first and use it over and over again.
# The module-level functions keep a cache of recently compiled patterns, so there isn’t a
# huge performance hit, but you’ll save a few lookups and extra processing by using your own compiled pattern.

for m in re.findall(r'(\d+)/(\d+)/(\d+)', 'Today is 11/27/2012. PyCon starts 3/13/2013.'):
    print(m)
