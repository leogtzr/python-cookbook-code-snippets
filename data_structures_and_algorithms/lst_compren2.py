import math

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

clip_neg = [n if n > 0 else 0 for n in mylist]
clip_pos = [0 if n > 0 else n for n in mylist]

print(clip_pos)
print(clip_neg)