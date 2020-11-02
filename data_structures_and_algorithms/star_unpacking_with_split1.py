line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
user_name, *fields, var_dir, sh = line.split(':')

print(user_name)
print(fields)
print(var_dir)
print(sh)
