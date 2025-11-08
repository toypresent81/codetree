n = int(input())
a = list(map(int, input().split()))

sort_nums = sorted(a, reverse= True)
print(sort_nums[0], sort_nums[1])