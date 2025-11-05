A, B = map(int, input().split())

print(f"{A//B}.", end="")

remainder = A % B

for _ in range(20):
    remainder *= 10
    print(remainder // B, end="")
    remainder = remainder % B