a, b = map(int, input().split())

def magic_number(a, b):
    count = 0
    for i in range(a, b+1):
        if is_prime(i) and calculate_sum(i):
            count += 1
    print(count)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def calculate_sum(n):
    total = 0
    for i in str(n):
        total += int(i)
    
    if total % 2 == 0:
        return True
    else:
        return False


magic_number(a, b)