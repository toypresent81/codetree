arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    if i == 0:
        break
    else:
        cnt += 1
arr = arr[0:cnt]
for i in arr[::-1]:
    print(i, end=" ")
