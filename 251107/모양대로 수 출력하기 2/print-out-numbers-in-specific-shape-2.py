N = int(input())
cnt = 0
for i in range(N):
    for j in range(N):
        if cnt % 10 == 8:
            cnt += 4
        else:
            cnt += 2
        print(cnt%10, end=" ")
    print()