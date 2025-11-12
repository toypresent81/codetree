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

def calculateArea(x1, y1):
    x1, y1 = x1 + OFFSET, y1 + OFFSET

    for x in range(x1, x1 + 8):
        for y in range(y1, y1 + 8):
            areas[x][y] = 1


for i in range(len(points)):    
    calculateArea(points[i][0], points[i][1])

area = 0
for x in range(MAX_RANGE + 1):
    for y in range(MAX_RANGE + 1):
        if areas[x][y] == 1:
            area += 1

print(area)
