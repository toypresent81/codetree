A, B = map(int, input().split())
cnt = 0
total = 0
for i in range(A, B+1):
    if i % 5 == 0 or i % 7 == 0:
        total += i  
        cnt += 1        
if cnt > 0:
    avg = total / cnt
    print(f"{total} {avg:.1f}")
else:
    print("0 0.0")

