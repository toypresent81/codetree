n = int(input())
arr = list(map(int, input().split()))

for i in range(1, n+1):
    if i % 2 == 1:
        odd_arr = arr[0:i]
        odd_arr.sort()
        index = len(arr[0:i])//2
        odd_arr[index]
        print(int(odd_arr[index]), end=" ")

