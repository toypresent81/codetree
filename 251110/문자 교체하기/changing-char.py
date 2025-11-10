a, b = input().split()
arr_a = list(a)
arr_b = list(b)
arr_b[0] = arr_a[0]
arr_b[1] = arr_a[1]
print("".join(arr_b))
