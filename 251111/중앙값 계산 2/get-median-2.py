n = int(input())
arr = list(map(int, input().split()))

arr.sort()

for i in range(1, n+1):
    if i % 2 == 1:
        avg = sum(arr[0:i])/len(arr[0:i])
        print(int(avg), end=" ")

