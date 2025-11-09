n = int(input())
arr = [
    input()
    for _ in range(n)
]
char = input()

count = 0
total = 0
for i in arr:
    if i[0] == char:
        count += 1
        total += len(i)
print(f"{count} {total/count:.2f}")