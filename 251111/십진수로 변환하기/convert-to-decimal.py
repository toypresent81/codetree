binary = input()

arr = list(binary)

num = 0
for i in range(len(arr)):
    num = num * 2 + int(arr[i])

print(num)