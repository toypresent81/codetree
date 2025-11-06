N = int(input())
prod = 1
cnt = 0
for i in range(1, 11):
    prod *= i
    cnt += 1
    if prod >= N:
        break
print(cnt)