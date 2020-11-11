n = int(input("n: "))

f = 1

for x in range(1, n+1):
    f *= x

print(f"{n}! = {f}")
