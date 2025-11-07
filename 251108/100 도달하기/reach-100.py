N = int(input())
arr = [1, N]
while True:    
    arr.append(arr[-1]+arr[-2])
    if arr[-1] >= 100:
        break
print(*arr)