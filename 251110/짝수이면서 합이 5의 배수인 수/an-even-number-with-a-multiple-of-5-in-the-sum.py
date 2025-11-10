n = int(input())

def magic_number(n):
    sum_val = n // 10 + n % 10
    if n % 2 == 0 and sum_val % 5 == 0:
        return "Yes"
    else:
        return "No"


print(magic_number(n))
