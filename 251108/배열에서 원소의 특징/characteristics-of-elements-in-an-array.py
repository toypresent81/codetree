arr = list(map(int, input().split()))
index = 0
for i in arr:
    index += 1
    if i % 3 == 0:       
        break
print(arr[index-2])
