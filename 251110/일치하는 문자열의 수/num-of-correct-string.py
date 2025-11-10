arr = input().split()
n = int(arr[0])
a = arr[1]

count = 0
for i in range(n):
    string = input()
    if a == string:
        count += 1
print(count)
