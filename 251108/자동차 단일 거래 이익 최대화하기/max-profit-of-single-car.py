n = int(input())
price = list(map(int, input().split()))

max_val = 0
for i in range(n):
    for j in range(i + 1, n):
        profit = price[j] - price[i]

        if profit > max_val:
            max_val = profit
    
print(max_val)