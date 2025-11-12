MAX_RANGE = 2000
offset = 1000

grid = [
    tuple(map(int, input().split()))
    for _ in range(3)
]
area_list = [
    [0]*(MAX_RANGE+1)
    for _ in range(MAX_RANGE+1)
]

def calculateArea(x1, y1, x2, y2, isDelete):
    x1, y1 = x1 + offset, y1 + offset
    x2, y2 = x2 + offset, y2 + offset

    for x in range(x1, x2):
        for y in range(y1, y2):
            if isDelete:
                area_list[x][y] = 2
            else:
                area_list[x][y] = 1

for i in range(len(grid)):    
    calculateArea(grid[i][0], grid[i][1], grid[i][2], grid[i][3], i==2)

area = 0
for x in range(MAX_RANGE+1):
    for y in range(MAX_RANGE+1):
        if area_list[x][y] == 1:
            area += 1

print(area)