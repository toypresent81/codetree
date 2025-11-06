while True:
    arr = input().split()
    a, b, char = int(arr[0]), int(arr[1]), arr[2]
    print(a*b)
    if char == "C":
        break