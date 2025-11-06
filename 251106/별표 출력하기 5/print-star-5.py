N = int(input())
for i in range(1, N+1):
    for _ in range(N, i-1, -1):
        for j in range(N, i-1, -1):
            print("*", end="")      
        print("", end=" ")
    print()    
