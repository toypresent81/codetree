arr = input().split()
C = arr[0]
N = int(arr[1])
if C == "A":
    for i in range(1, N+1):
        print(i, end=" ")
else:
    for i in range(N, 0, -1):
        print(i, end=" ")
