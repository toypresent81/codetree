n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

num = 1

for i in range(n + m - 1): # 대각선의 개수,  행(j) + 열 = i (대각선 번호), 
    for j in range(n):
        if 0 <= i - j < m: # i - j = 열 번호가 음수가 아니고 m을 넘지 않음
            arr[j][i - j] = num
            num += 1

for row in arr:
    print(*row)
