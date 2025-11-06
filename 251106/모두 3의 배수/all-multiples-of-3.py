cnt = 0
for i in range(5):
    num = int(input())
    if num % 3 == 0:
        cnt += 1
print("1" if cnt == 5 else "0")