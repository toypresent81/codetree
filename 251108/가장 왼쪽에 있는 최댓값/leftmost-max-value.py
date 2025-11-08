n = int(input())
a = list(map(int, input().split()))

max_num = max(a)
print(a.index(max_num)+1, end=" ")
while max_num != a[0]:
    if max_num in a:
        a = a[:a.index(max_num)]
        max_num = max(a)
        print(a.index(max_num)+1, end=" ")
