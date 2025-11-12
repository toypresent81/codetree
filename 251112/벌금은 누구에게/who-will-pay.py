N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

nums_of_students = [0] * (N+1)

ans = 0
for i in range(M):    
    for idx, num in enumerate(student):
        nums_of_students[num] += 1
        if nums_of_students[num] >= K:
            ans = num
            break

print(ans)
