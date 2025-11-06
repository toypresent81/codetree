N = int(input())
cnt = 0
total = 0
for i in range(N):
    num = int(input())
    cnt += 1
    total += num
print(f"{total} {total/cnt:.1f}")