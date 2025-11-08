A, B = map(int, input().split())
remainders = [0 for _ in range(11)]

while A > 1:
    A //= B
    remainders[A % B] += 1

total = 0
for i in remainders:
    total += i*i
print(total)
