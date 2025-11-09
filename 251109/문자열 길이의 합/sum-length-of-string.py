n = int(input())
total = 0
count = 0
for i in range(n):
    char = input()
    total += len(char)
    if char[0] == "a":
        count += 1
print(total, count)