N1, N2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if B[0] in A:
    first_idx = A.index(B[0])
    if A[first_idx:first_idx+len(B)] == B:
        print("Yes")
    else:
        print("No")
else:
    print("No")            



