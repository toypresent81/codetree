n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

blocks = [0 for _ in range(20+1)]


start = 0
end = 0
for i in range(n):
    if dir[i] == "L":
        start = end - x[i]
    else:
        end = start + x[i]
    
    for j in range(start, end):
        blocks[j-1] += 1

count = 0
for i in blocks:
    if i >= 2:
        count += 1
print(count+1)
