arr = list(map(int, input().split()))
if 0 in arr:
    arr = arr[:arr.index(0)] 
for i in arr:
    if i % 2 == 1:
        print(i+3, end=" ")
    else:
        print(i//2, end=" ")
