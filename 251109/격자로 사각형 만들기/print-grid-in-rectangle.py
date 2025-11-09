n = int(input())
arr_2d = [[1 for _ in range(n)] for _ in range(n)]
for row in range(n):
    for col in range(n):
        if row == 0 or col == 0:
            arr_2d[row][col] = 1
        else:
            arr_2d[row][col] = arr_2d[row][col-1] + arr_2d[row-1][col] + arr_2d[row-1][col-1]

for row in range(n):
    for col in range(n):
        print(arr_2d[row][col], end=" ")
    print()