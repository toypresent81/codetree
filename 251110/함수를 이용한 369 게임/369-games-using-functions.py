a, b = map(int, input().split())

def magic_number(a, b):
    count = 0
    for i in range(a, b+1):
        if i % 3 == 0:
            count += 1
        else:
            if three_number(i):
                count += 1

    print(count)


def three_number(i):
    for j in str(i):
        if j == "3" or j == "6" or j == "9":
            return True            
    return False


magic_number(a, b)
