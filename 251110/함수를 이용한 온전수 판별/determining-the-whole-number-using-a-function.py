a, b = map(int, input().split())

def perfect_num(a, b):
    count = 0
    for i in range(a, b+1):
        if i % 2 != 0 and i % 5 != 0 and (i % 3 != 0 or i % 9 == 0):
            count += 1
    print(count)
            

perfect_num(a, b)
