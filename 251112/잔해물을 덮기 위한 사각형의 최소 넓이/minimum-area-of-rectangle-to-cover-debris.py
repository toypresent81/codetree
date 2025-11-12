MAX_RANGE = 2000
OFFSET = 1000

x1_1, y1_1, x2_1, y2_1 = map(int, input().split())
x1_2, y1_2, x2_2, y2_2 = map(int, input().split())

areas = [
    [0] * (MAX_RANGE + 1) 
    for _ in range(MAX_RANGE + 1)
]

for x in range(x1_1 + OFFSET, x2_1 + OFFSET):
    for y in range(y1_1 + OFFSET, y2_1 + OFFSET):
        areas[x][y] = 1

for x in range(x1_2 + OFFSET, x2_2 + OFFSET):
    for y in range(y1_2 + OFFSET, y2_2 + OFFSET):
        areas[x][y] = 0

min_x = MAX_RANGE + 1
max_x = -1
min_y = MAX_RANGE + 1
max_y = -1

for x in range(MAX_RANGE + 1):
    for y in range(MAX_RANGE + 1):
        if areas[x][y] == 1:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

if max_x >= min_x and max_y >= min_y:
    area = (max_x - min_x + 1) * (max_y - min_y + 1)
    print(area)
else:
    print(0)