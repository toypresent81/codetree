string = input()
arr = list(string)
first = arr[0]
second = arr[1]

for i in range(len(arr)):
    if arr[i] == second:
        arr[i] = first
    elif arr[i] == first:
        arr[i] = second
print("".join(arr))
