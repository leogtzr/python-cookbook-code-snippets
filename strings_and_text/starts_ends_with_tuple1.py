filenames = ['Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h']

for fn in [name for name in filenames if name.endswith(('.c', '.h'))]:
    print(fn)

is_there_a_python_file = any(name.endswith('.py') for name in filenames)
print(is_there_a_python_file)
