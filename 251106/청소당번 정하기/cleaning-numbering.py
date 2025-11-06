n = int(input())
classroom, corridor, toilet = 0, 0, 0

for i in range(n+1):
    if i % 2 == 0 and i % 6 != 0 and i % 12 != 0:
        classroom += 1
    if i % 3 == 0 and i % 12 != 0:
        corridor += 1
    if i >= 12 and i % 12 == 0:
        toilet += 1

print(classroom, corridor, toilet)
