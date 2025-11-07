N = int(input())
matrix = [ [0 for _ in range(N)] for _ in range(N) ]
for i in range(N):
    for j in range(N):
        if i % 2 == 0:
            matrix[i][j] = j + 1            
        else:
            matrix[i][j] = N - j            

for i in range(N):
    for j in range(N):
        print(matrix[j][i], end="")
    print()