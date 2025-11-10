string = input()
arr = list(string)
for i in range(len(arr)):
    if arr[i] == "e":
        arr = arr[:i] + arr[i+1:]
        print("".join(arr))
        break
