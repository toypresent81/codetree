a, b = input().split()
sum_val = ord(a)+ord(b)
sub_val = 0
if ord(a) > ord(b):
    sub_val = ord(a) - ord(b)
else:
    sub_val = ord(b) - ord(a)
print(sum_val, sub_val)