n = int(input())

def return_val(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total // 10


print(return_val(n))
