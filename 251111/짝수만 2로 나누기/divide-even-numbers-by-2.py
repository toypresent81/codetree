n = int(input())
arr = list(map(int, input().split()))

def remain(n, arr):
    for i in range(n):
        if arr[i] % 2 == 0:
            arr[i] //= 2

    return arr


for i in remain(n, arr):
    print(i, end=" ")




