a, b = map(int, input().split())

def calculate_numbers(a, b):
    if a > b:
        a *= 2
        b += 10
        return a, b
    else:
        b *= 2
        a += 10
        return a, b


a, b = calculate_numbers(a, b)
print(a, b)
