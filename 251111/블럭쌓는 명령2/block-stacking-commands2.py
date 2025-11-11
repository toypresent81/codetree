n, k = map(int, input().split())

blocks = [0 for _ in range(n)]

for i in range(k):
    a, b = map(int, input().split())
    cnt = 0
    for j in range(a, b+1):
        cnt += 1
        blocks[j] = cnt

print(max(blocks))