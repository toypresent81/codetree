N = int(input())

for i in range(N):
    for j in range(N):
        if (i and j) != 0 and (i and j) != N-1 and i <= j:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()