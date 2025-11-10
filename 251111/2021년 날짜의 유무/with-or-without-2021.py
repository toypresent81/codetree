M, D = map(int, input().split())

def check_date(m, n):
    if check_month(m) and check_day(m, n):
        print("Yes")
    else:
        print("No")

def check_month(m):
    if m >= 1 and m <= 12:
        return True
    else:
        return False

def check_day(m ,d):
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        if d >= 1 and d <= 31:
            return True
        else:
            return False
    elif m == 2:
        if d >= 1 and d <= 28:
            return True
        else:
            return False
    else:
        if d >= 1 and d <= 30:
            return True
        else:
            return False


check_date(M, D)