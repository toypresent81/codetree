n = int(input())
blocks = [0 for _ in range(100+1)]

for i in range(n):
    a, b = map(int, input().split())
    for j in range(a, b+1):
        blocks[j] += 1

print(max(blocks))
