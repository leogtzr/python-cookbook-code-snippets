from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])

sub = Subscriber('leogutierrezramirez@gmail.com', '2020-11-07')

# print(sub)

# print(sub.addr)
# print(sub.joined)

addr, joined = sub

print(addr)
print(joined)

