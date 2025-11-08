arr = list(map(int, input().split()))
grades = [0 for _ in range(11)]

for i in arr:
    if i == 0:
        break
    if i // 10 != 0:
        grades[i//10] += 1

for i in range(10, 0, -1):
    print(f"{i*10} - {grades[i]}")
    