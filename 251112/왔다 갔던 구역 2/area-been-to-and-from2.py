n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

blocks = [0 for _ in range(200+2)]

current = 100
for i in range(n):
    if dir[i] == "L":
        start = current - x[i]
        end = current
    else:
        start = current
        end = current + x[i]
    
    for j in range(start, end):
        blocks[j] += 1

    current = end if dir[i] == "R" else start

count = 0
for i in blocks:
    if i >= 2:
        count += 1
print(count)
