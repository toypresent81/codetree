arr = [input() for _ in range(10)]
a = input()

count = 0
for i in arr:
    if i[-1] == a:
        print(i)
        count += 1
if count == 0:
    print("None")