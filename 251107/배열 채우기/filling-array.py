arr = list(map(int, input().split()))
if len(arr) == 10:
    for i in arr[::-1]:
        print(i, end=" ")
else:
    arr.pop()
    for i in arr[::-1]:
        print(i, end=" ")
