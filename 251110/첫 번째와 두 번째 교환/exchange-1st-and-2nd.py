string = input()
arr = list(string)
first = arr[0]
second = arr[1]

for i in range(len(arr)):
    if i == 0:
        arr[0] = second
    elif i == 1:
        arr[1] = first
    else:
        if arr[i] == second:
            arr[i] = first
        if arr[i] == first:
            arr[i] = second
print("".join(arr))
