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
    if i // 10 == 3 or i % 10 == 3:
        return True
    elif i // 10 == 6 or i % 10 == 6:
        return True
    elif i // 10 == 9 or i % 10 == 9:
        return True
    else:
        return False


magic_number(a, b)
