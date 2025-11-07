arr = list(map(int, input().split()))
total = 0
cnt = 0
for i in arr:
    if i >= 250:
        break
    else:
        total += i
        cnt += 1
print(f"{total} {total/cnt:.1f}")  


