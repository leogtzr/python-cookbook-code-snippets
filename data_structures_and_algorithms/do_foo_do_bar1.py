records = [
    ('foo', 1, 2),
    ('bar', 2, 3),
    ('foo', 4, 5),
]

def do_foo(vals):
    print('I am doing foo')
    print(vals)

def do_bar(vals):
    print('I am doing bar')
    print(vals)

for tag, *vals in records:
    if tag == 'foo':
        do_foo(vals)
    elif tag == 'bar':
        do_bar(vals)

