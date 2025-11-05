a, b, c = map(int, input().split())
if a <= b and b <= c:
    print("1", end=" ")
elif a <= b and b >= c:
    if a <= c:
        print("1", end=" ")
    else:
        print("0", end=" ")
else:
    print("0", end=" ")

if a == b == c:
    print("1")
else:
    print("0")