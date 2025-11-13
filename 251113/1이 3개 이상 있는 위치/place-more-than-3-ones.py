n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def find_count(x, y):
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    count = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[nx][ny] == 1:
            count += 1

    return count   

ans = 0
for i in range(n):
    for j in range(n):
        if find_count(i, j) >= 3:
            ans += 1

print(ans)

