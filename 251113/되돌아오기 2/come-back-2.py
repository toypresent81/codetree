commands = input()

dirs = list(commands)

dir_num = 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

x, y = 0, 0
time = 0
isStart = False
for dir in dirs:
    if dir == "F":
        x += dx[dir_num]
        y += dy[dir_num]
    elif dir == "R":
        dir_num = (dir_num + 1) % 4
    else:
        dir_num = (dir_num - 1 + 4) % 4

    time += 1
    if x == 0 and y == 0:
        isStart = True
        break

print(time if isStart == True else -1)