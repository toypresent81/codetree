N, M = map(int, input().split())
count = 0
for i in range(N):
    for j in range(M):
        count += 1
        print(count, end=" ")
    print()