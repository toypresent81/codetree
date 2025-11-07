N = int(input())
for i in range(1, N+1):
    for j in range(1, N-i+2):
        if j == N-i+1:
            print(f"{i} * {j} = {i*j}", end="\n")
        else:
            print(f"{i} * {j} = {i*j}", end=" / ")