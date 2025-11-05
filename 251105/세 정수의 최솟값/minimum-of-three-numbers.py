a, b, c = map(int, input().split())
if a >= b and b >= c:
    print(c)
elif a >= b and c >= b:
    print(b)
elif b >= a and b >= c:
    if a >= c:
        print(c)
    else:
        print(a)
else:
    print(a)