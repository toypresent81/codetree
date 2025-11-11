n = int(input())
blocks = [0 for _ in range(200+1)]

for i in range(n):
    a, b = map(int, input().split())
    for j in range(a, b):
        blocks[j] += 1

print(max(blocks))

