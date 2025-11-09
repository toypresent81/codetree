n = int(input())
arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

num = 1
if n % 2 == 0:    
    for col in range(n - 1, -1, -1):
        if col % 2 == 0:
            for row in range(n):
                arr_2d[row][col] = num
                num += 1
        else:
            for row in range(n - 1, -1, -1):
                arr_2d[row][col] = num
                num += 1
else:
    for col in range(n - 1, -1, -1):
        if col % 2 == 1:
            for row in range(n):
                arr_2d[row][col] = num
                num += 1
        else:
            for row in range(n - 1, -1, -1):
                arr_2d[row][col] = num
                num += 1

for row in range(n):
    for col in range(n):
        print(arr_2d[row][col], end = ' ')
    print()
        