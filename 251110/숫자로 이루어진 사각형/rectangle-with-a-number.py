n = int(input())

def print_rect(n):
    count = 0
    for i in range(n):
        for j in range(n):
            if count % 10 == 9:
                count += 2
            else:
                count += 1
            print(count % 10, end=" ")
        print()


print_rect(n)