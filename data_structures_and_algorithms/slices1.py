a = slice(5, 50, 2)
# print(a)

print(a.start)
print(a.stop)
print(a.step)

s = 'HelloWorld'
for i in range(*a.indices(len(s))):
    print(s[i])

