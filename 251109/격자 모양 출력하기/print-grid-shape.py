n, m = map(int, input().split())
arr_2d = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    r, c = map(int, input().split())
    arr_2d[r-1][c-1] = r*c

for i in range(n):
    for j in range(n):
        print(arr_2d[i][j], end=" ")
    print()
