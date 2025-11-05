A, B, C = map(int, input().split())
if A >= B and B >= C:
    print(B)
elif A >= B and C >= B:
    if A >= C:
        print(C)
    else:
        print(A)
elif A <= B and B >= C:
    if A >= C:
        print(A)
    else:
        print(C)
else:
    print(B)