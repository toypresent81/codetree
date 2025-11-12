n = int(input())
arr = [int(input()) for _ in range(n)]

max_val = 1
count = 1
for i in range(n):
    if i == 0 or arr[i] == arr [i-1]:
        count += 1
        if max_val < count:
            max_val = count
    elif arr[i] != arr [i-1]:
        count = 1
print(max_val)