M = int(input())
for _ in range(M):
    cnt = 0
    N = int(input())
    while N != 1:
        if N % 2 == 1:
            N = 3 * N + 1
            cnt += 1
        else:
            N /= 2
            cnt += 1
    print(cnt)

    