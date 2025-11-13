n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

x, y = 0, 0
for i in range(n):
    if dir[i] == "N":
        x, y = x, y + dist[i]
    elif dir[i] == "S":
        x, y = x, y - dist[i]
    elif dir[i] == "E":
        x, y = x + dist[i] , y
    else:
        x, y = x - dist[i] , y

print(x, y)



