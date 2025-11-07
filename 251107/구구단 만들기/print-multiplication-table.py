A, B = map(int, input().split())
for i in range(1, 10):
    for j in range(1, B//2+1):
        if j == B//2:
            print(f"{B-2*(j-1)} * {i} = {(B-2*(j-1)) * i}", end=" ")
        else:
            print(f"{B-2*(j-1)} * {i} = {(B-2*(j-1)) * i}", end=" / ")
    print()