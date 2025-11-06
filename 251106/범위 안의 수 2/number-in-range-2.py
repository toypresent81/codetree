total = 0
cnt = 0
for i in range(10):
    num = int(input())
    if num >= 0 and num <= 200:
        total += num
        cnt += 1
print(f"{total} {total/cnt:.1f}")