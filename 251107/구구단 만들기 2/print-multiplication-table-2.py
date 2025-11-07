A, B = map(int, input().split())
for i in range(2, 9, 2):
    for j in range(B, A-1, -1):
        if j == A:
            print(f"{j} * {i} = {j*i}", end="")
        else:
            print(f"{j} * {i} = {j*i}", end=" / ")
    print()