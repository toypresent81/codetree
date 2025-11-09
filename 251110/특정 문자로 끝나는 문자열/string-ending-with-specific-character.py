arr = [0 for _ in range(10)]
for i in range(10):
    char = input()
    arr[i] = char
a = input()

count = 0
for i in arr:
    if i[-1] == a:
        print(i)
        count += 1
if count == 0:
    print("None")