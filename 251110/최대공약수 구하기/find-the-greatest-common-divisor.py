n, m = map(int, input().split())

def print_max(n, m):
    arr_a = []
    for i in range(1, n+1):
        if n % i == 0:
            arr_a.append(i)
    
    arr_b = []
    for i in range(1, m+1):
        if m % i == 0:
            arr_b.append(i)

    max_val = []
    for i in arr_a:
        for j in arr_b:
            if i == j:
                max_val.append(i)

    print(max(max_val))


print_max(n, m)
