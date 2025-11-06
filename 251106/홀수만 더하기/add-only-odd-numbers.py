N = int(input())
total = 0
for _ in range(N):
    num = int(input())
    if num % 2 == 1 and num % 3 == 0:
        total += num
print(total)
