N = int(input())
cnt = 0
for i in range(N):
    grades = list(map(int, input().split()))
    total = sum(grades)
    avg = total / len(grades)
    if avg >= 60:
        print("pass")
        cnt += 1
    else:
        print("fail")
print(cnt)