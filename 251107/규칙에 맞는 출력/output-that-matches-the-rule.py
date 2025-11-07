N = int(input())
for i in range(1, N+1):
    for j in range(i):
        print(N-i+1+j, end=" ")
    print()