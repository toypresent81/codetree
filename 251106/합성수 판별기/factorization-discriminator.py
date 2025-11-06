N = int(input())

cnt = 0
for i in range(2, N):
    if N % i == 0:
        cnt += 1
print("C" if cnt != 0 else "N")