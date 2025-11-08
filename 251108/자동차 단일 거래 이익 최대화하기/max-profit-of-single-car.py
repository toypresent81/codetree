n = int(input())
price = list(map(int, input().split()))
buy = price[0]

for i in range(1, n):
    if buy > price[i]:
        buy = price[i]
        min_idx = i
        sell = price[i]
        for j in range(min_idx+1, n):
            if sell < price[j]:
                sell = price[j]


profit = sell - buy

print(profit)