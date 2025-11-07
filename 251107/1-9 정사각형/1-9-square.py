N = int(input())
cnt = 0
for i in range(N):
    for j in range(N):   
        if cnt % 10 == 9:
            cnt += 2
        else:
            cnt +=1
        print(cnt%10, end="")
    print()