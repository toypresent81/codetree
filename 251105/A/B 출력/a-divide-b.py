A, B = map(int, input().split())

a = A//B
n = A%B
print(f"{a}.", end="")
for _ in range(20):
    if a == 0:
        A *= 10
        print(f"{A//B}", end="")
        A = A % B
    else:
        A = n * 10
        print(f"{A//B}", end="")