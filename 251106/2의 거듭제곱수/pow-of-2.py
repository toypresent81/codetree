N = int(input())

i = 1
while N > 2:
    N //= 2
    i += 1
print(i)