arr = list(map(int, input().split()))
if 0 in arr:
    arr = arr[:arr.index(0)]

total = 0
cnt = 0
for i in arr:
    if i % 2 == 0:
        cnt += 1
        total += i
print(cnt, total)