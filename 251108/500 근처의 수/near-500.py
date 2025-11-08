arr = list(map(int, input().split()))
sort_arr = sorted(arr)

index = 0
for idx, num in enumerate(sort_arr):
    if num > 500:
        index = idx
        break
print(sort_arr[index-1], sort_arr[index])