n = int(input())
arr = list(map(int, input().split()))

def absolute_number(n, arr):
    for i in range(n):
        arr[i] = abs(arr[i])    
    return arr


for i in absolute_number(n, arr):
    print(i, end=" ")