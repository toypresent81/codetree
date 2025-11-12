n = int(input())

MAX_RANGE = 200
OFFSET = 100

points = [
    tuple(map(int, input().split())) 
    for _ in range(n)
]
areas = [
    [0] * (MAX_RANGE + 1)
    for _ in range(MAX_RANGE + 1)
]

for i in range(n):
    x1, y1 = points[i][0] + OFFSET, points[i][1] + OFFSET
    x2, y2 = points[i][2] + OFFSET, points[i][3] + OFFSET

    for x in range(x1, x2):
        for y in range(y1, y2):
            if i % 2 == 0:
                areas[x][y] = 1
            else:
                areas[x][y] = 2

area = 0
for x in range(MAX_RANGE+1):
    for y in range(MAX_RANGE+1):
        if areas[x][y] == 2:
            area += 1
print(area)

