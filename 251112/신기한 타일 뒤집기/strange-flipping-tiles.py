n = int(input())

blocks = [''] * 200002
current = 100000

for _ in range(n):
    distance, direction = input().split()
    distance = int(distance)
    
    if direction == "L":
        for j in range(current - distance + 1, current + 1):
            blocks[j] += "W"
        current -= (distance - 1) 
    else:
        for j in range(current, current + distance):
            blocks[j] += "B"
        current += (distance - 1)

w, b = 0, 0
for block in blocks:
    if block and block[-1] == 'W':
        w += 1
    elif block and block[-1] == 'B':
        b += 1

print(w, b)