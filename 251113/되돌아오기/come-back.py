N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

dir_num = 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

x, y = 0, 0
time = 0
found = False

for i in range(N):
    for _ in range(dist[i]):
        if dir[i] == "N":
            dir_num = 0
        elif dir[i] == "E":
            dir_num = 1
        elif dir[i] == "S":
            dir_num = 2
        else:
            dir_num = 3

        x += dx[dir_num]
        y += dy[dir_num]
        time += 1

        if x == 0 and y == 0:
            found = True
            break
    if found:
        break

print(time if found == True else -1)






