a, b, c, d = map(int, input().split())

from_time = a * 60 + b
to_time = c * 60 + d
print(to_time - from_time)