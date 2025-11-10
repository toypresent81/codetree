n = int(input())
total = 0
for i in range(n):
    num = int(input())
    total += num

total_str = str(total)
total_str = total_str[1:] + total_str[0]
print(total_str)
