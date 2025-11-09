arr_2d = [list(map(int, input().split())) for _ in range(4)]
sum_val = 0
for i in range(1, 5):
    for j in range(i):
        sum_val += arr_2d[i-1][j]
print(sum_val)