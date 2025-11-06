N = int(input())
for i in range(1, 2*N+1):
    if i % 2 == 1:
        for j in range(N-i//2):
            print("*", end=" ")
        print()
    else:
        for j in range(i//2):
            print("*", end=" ")
        print()
        

