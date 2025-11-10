a, b = map(int, input().split())
sum_val = a + b
count = 0
for i in str(sum_val):
    if i == "1":
        count += 1
print(count)