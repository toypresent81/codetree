n = int(input())
arr_2d = [[0 for _ in range(n)] for _ in range(n)]
for row in range(1, n+1):
    for col in range(1, row+1):
        if row == 0 or row == 1 or col == 1:
            arr_2d[row-1][col-1] = 1
        else:
            arr_2d[row-1][col-1] = arr_2d[row-2][col-2] + arr_2d[row-2][col-1]

for row in range(1, n+1):
    for col in range(1, row+1):
        print(arr_2d[row-1][col-1], end=" ")
    print()
