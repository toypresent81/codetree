N = int(input())
total = 0
cnt = 0
for i in range(1, 101):   
    total += i
    cnt += 1 
    if total >= N:
        break
        
print(cnt)
