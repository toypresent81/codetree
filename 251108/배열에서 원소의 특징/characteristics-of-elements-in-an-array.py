arr = list(map(int, input().split()))
index = 0
for i in arr:
    if i % 3 == 0:
        index += 1
print(arr[index-2])
