n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]


def sum_value(m, queries):
    global arr    
    for i in range(m):
        total = 0
        for j in range(queries[i][0], queries[i][1]+1):
            total += arr[j-1]
        print(total)

sum_value(m, queries)