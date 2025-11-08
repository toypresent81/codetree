N, Q = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(Q):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        print(nums[arr[1]-1])
    elif arr[0] == 2:
        if arr[1] in nums:
            print(nums.index(arr[1])+1)
        else:
            print(0)
    else:
        for i in range(arr[1], arr[2]+1):
            print(nums[i-1], end=" ")
        print()


