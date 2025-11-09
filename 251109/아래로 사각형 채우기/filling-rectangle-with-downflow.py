N = int(input())
arr_2d = [[0 for _ in range(N)] for _ in range(N)]
count = 0
for i in range(N):
    for j in range(N):
        count += 1
        arr_2d[i][j] = count

for i in range(N):
    for j in range(N):
        print(arr_2d[j][i], end=" ")
    print()