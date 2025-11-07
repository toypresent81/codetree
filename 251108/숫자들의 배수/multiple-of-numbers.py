N = int(input())
arr = [ N * i for i in range(1, N * 11) ]
cnt = 0
for i in arr:
    if cnt == 2:        
        break    
    if i % 5 == 0:
        cnt += 1
    print(i, end=" ")