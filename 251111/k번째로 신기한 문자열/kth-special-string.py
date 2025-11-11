n, k, t = input().split()
n, k = int(n), int(k)

arr = []
for i in range(n):
    str = input()
    if str[:len(t)] == t:
        arr.append(str)

arr.sort()
print(arr[2])