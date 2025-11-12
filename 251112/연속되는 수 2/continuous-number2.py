n = int(input())
arr = [int(input()) for _ in range(n)]

result = [1]
count = 1
for i in range(n):
    if i == 0 or arr[i] == arr [i-1]:
        count += 1         
    elif arr[i] != arr[i-1]:
        result.append(count)
        count = 1
print(max(result))