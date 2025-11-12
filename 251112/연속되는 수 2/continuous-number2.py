n = int(input())
arr = [int(input()) for _ in range(n)]


result, cnt = 0, 0
for i in range(n):
    if i >= 1 or arr[i] == arr[i-1]:
        count += 1         
    else
        count = 1
    result = max(result, cnt)

print(max(result))