n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

mapper = {
    "R": 0,
    "D": 1,
    "U": 2,
    "L": 3
}

x, y = r-1, c-1
move_dir = mapper[d]

for i in range(t):    
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    if not in_range(nx, ny):
        move_dir = 3 - move_dir
    else:
        x, y = nx, ny

print(x+1, y+1)    