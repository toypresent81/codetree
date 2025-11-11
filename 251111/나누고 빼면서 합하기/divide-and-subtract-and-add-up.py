n, m = map(int, input().split())
A = list(map(int, input().split()))

def caculate(m, A):
    total = 0
    while m >= 1:
        total += A[m-1]

        if m % 2 == 1:
            m -= 1
        else:
            m //= 2
    return total

print(caculate(m, A))