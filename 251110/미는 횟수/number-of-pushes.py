a = input()
b = input()

count = 0
for i in a:
    a = a[1:] + a[0]
    count += 1
    if a == b:
        break
print(count if a == b else -1)
