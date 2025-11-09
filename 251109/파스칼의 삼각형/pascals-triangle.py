n = int(input())
arr_2d = [[" " for _ in range(n)] for _ in range(n)]
for row in range(n):
    for col in range(row + 1):
        if col == 0 or col == row:
            arr_2d[row][col] = 1
        else:
            arr_2d[row][col] = arr_2d[row-1][col-1] + arr_2d[row-1][col]

for row in arr_2d:
    for col in row:
        print(col, end=" ")
    print()
