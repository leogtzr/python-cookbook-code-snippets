def head_ls(values):
    head, *_ = values
    return head

def tail_ls(values):
    *_, tail = values
    return tail

name = 'Leonardo'

print(head_ls(name))
print(tail_ls(name))
