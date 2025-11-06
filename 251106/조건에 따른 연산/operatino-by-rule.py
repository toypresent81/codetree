N = int(input())
cnt = 0
while N < 1000:
    if N % 2 == 0:
        N = 3 * N + 1
        cnt += 1
    else:
        N = 2 * N + 2
        cnt += 1
print(cnt)