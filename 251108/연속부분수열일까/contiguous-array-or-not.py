N1, N2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

satisfied = False
if B[0] in A:
    for idx, num in enumerate(A):
        if num == B[0]:
            if A[idx:idx+len(B)] == B:
                satisfied = True
                break
            else:
                continue
        else:
            continue
else:
    satisfied = False        
print("Yes" if satisfied == True else "No")



