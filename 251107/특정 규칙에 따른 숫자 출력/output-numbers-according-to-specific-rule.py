N = int(input())
cnt = 0
for i in range(1, N+1):
    for j in range(i-1):
        print(" ", end=" ")
    for j in range(N-i+1, 0, -1):
        
        if cnt % 10 == 9:
            cnt += 2
        else:
            cnt += 1
        print(cnt % 10, end=" ")
    print()