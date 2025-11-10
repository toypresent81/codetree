a, b = input().split()
index_a, index_b = 0, 0
for idx, char in enumerate(a):
    if char.isdigit() == False:
        index_a = idx
for idx, char in enumerate(b):
    if char.isdigit() == False:
        index_b = idx

print(int(a[:index_a])+int(b[:index_b]))