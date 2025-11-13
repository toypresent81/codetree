dirs = input()
arr = list(dirs)
dir_num = 3
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

x, y = 0, 0
for i in arr:
    if i == "L":
        dir_num = (dir_num - 1 + 4) % 4
    elif i == "R":
        dir_num = (dir_num + 1) % 4
    else:
        x += dx[dir_num]
        y += dy[dir_num]
print(x, y)