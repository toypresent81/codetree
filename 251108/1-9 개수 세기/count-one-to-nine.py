N = int(input())
numbers = [0 for _ in range(9)]
arr = list(map(int, input().split()))

for i in arr:
    numbers[i-1] += 1

for i in range(9):
    print(numbers[i])

