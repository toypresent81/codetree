arr_2d = [
    [0 for _ in range(5)]
    for _ in range(5)
]
for row in range(5):
    for col in range(5):
        if row == 0 or col == 0:
            arr_2d[row][col] = 1
        else:
            arr_2d[row][col] = arr_2d[row][col-1] + arr_2d[row-1][col]

for row in range(5):
    for col in range(5):
        print(arr_2d[row][col], end=" ")
    print()