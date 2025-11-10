n, m = map(int, input().split())

def print_rect(n, m):
    for i in range(n):
        for j in range(m):
            print("1", end="")
        print()


print_rect(n, m)