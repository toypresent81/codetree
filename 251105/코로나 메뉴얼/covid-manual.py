info1 = input().split()
info2 = input().split()
info3 = input().split()

info = [info1, info2, info3]

cnt = 0
for i in info:
    if i[0] == "Y" and int(i[1]) >= 37:
        cnt += 1
    else:
        continue
print("E" if cnt >= 2 else "N")


