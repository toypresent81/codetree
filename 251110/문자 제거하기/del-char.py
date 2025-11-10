string = input()
arr = list(string)
while len(arr) != 1:
    n = int(input())
    if n > len(arr):
        arr.pop(-1)
    else:
        arr.pop(n)
    print("".join(arr))