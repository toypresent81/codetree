start, end = map(int, input().split())

cnt = 0
for i in range(start, end+1):
    total = 0
    for j in range(1, i+1):        
        if i % j == 0:
            total += j
    if total-i == i:
        cnt += 1
print(cnt)


