N = int(input())
for i in range(N):
    for j in range(N):
        if i % 2 == 0:
            print(j + 1, end="")
        else:
            print(N - j, end="")
    print()