N = int(input())
cnt = 0
for i in range(1, N+1):
    for j in range(i):
        if cnt % 26 == 0:
            cnt = 1
        else:
            cnt += 1
        print(chr(ord("A")+cnt-1), end="")
    print()
