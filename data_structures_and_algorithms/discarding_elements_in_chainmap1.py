0 🐧 leo@lein ~/code/python/python-cookbook-code-snippets/data_structures_and_algorithms (main) $ p3
Python 3.8.6 (default, Sep 25 2020, 09:36:53) 
[GCC 10.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> values = ChainMap()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ChainMap' is not defined
>>> from collections import ChainMap
>>> values = ChainMap()
>>> values
ChainMap({})
>>> values['x'] = 1
>>> values
ChainMap({'x': 1})
>>> values = values.new_child()
>>> values['x'] = 2
>>> values
ChainMap({'x': 2}, {'x': 1})
>>> values = values.new_child()
>>> values
ChainMap({}, {'x': 2}, {'x': 1})
>>> values['x'] = 3
>>> values
ChainMap({'x': 3}, {'x': 2}, {'x': 1})
>>> # Discard last mapping
>>> values = values.parents
>>> values
ChainMap({'x': 2}, {'x': 1})
>>> values = values.parents
>>> values
ChainMap({'x': 1})
>>> 


