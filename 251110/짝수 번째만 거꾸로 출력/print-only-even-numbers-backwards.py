a = input()
arr = []
for i in range(len(a)):
    if i % 2 == 1:
        arr.append(a[i])

arr.reverse()
for i in arr:
    print(i, end="")

