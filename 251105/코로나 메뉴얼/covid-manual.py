cnt = 0
for _ in range(3):
    a, b = input().split()
    if a == "Y" and int(b) >= 37:
        cnt += 1
    else:
        continue
print("E" if cnt >= 2 else "N")