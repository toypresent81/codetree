a, b = map(int, input().split())

def calculate(a, b):
    if a > b:
        a += 25
        b *= 2
        return a, b
    else:
        b += 25
        a *= 2
        return a, b

a, b = calculate(a, b)
print(a, b)

