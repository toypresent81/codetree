N = int(input())
total = 0
cnt = 0
for i in range(1, 101):    
    if total > N:
        break
    else:
        total += i
        cnt += 1
print(cnt)
