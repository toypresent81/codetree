arr = list(map(int, input().split()))

if 0 in arr:
    arr = arr[:arr.index(0)]
    
total = sum(arr)
avg = sum(arr) / len(arr)
print(f"{total} {avg:.1f}")
