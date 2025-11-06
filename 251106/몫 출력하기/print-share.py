i = 0
while i < 3:
    num = int(input())
    if num % 2 == 1:
        continue
    else:
        print(num // 2)
        i += 1