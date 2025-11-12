n, m = map(int, input().split())

MAX_RANGE = 1000000
ans_a = [0] * (MAX_RANGE + 1)
ans_b = [0] * (MAX_RANGE + 1)

time_a, time_b = 1, 1
for _ in range(n):
    direction, time = input().split()
    for i in range(int(time)):
        ans_a[time_a] = ans_a[time_a - 1] + (1 if direction == "R" else -1)
        time_a += 1
        
for _ in range(m):
    direction, time = input().split()
    for i in range(int(time)):
        ans_b[time_b] = ans_b[time_b - 1] + (1 if direction == "R" else -1)
        time_b += 1

ans = -1
for i in range(1, min(time_a, time_b)):
    if ans_a[i] == ans_b[i]:
        ans = i
        break
print(ans)