arr = list(map(int, input().split()))
dices = [0 for _ in range(6)]

for i in arr:
    dices[i-1] += 1

for i in range(1, 7):
    print(f"{i} - {dices[i-1]}")