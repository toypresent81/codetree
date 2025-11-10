a, b, c = map(int, input().split())

def find_min(a, b, c):
    if a >= b and b >= c:
        return c
    elif a >= b and c >= b:
        return b
    elif b >= a and b >= c:
        if a >= c:
            return c
        else:
            return a
    else:
        return a


print(find_min(a, b, c))