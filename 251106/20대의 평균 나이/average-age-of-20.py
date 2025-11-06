total = 0
cnt = 0
while True:
    age = int(input())
    if age // 10 != 2:
        break
    else:
        total += age
        cnt += 1
print(f"{total/cnt:.2f}")