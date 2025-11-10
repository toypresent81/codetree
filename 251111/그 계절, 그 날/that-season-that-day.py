Y, M, D = map(int, input().split())

def check_season(y, m, d):
    if check_date(y, m, d):
        if m >= 3 and m <= 5:
            print("Spring")
        elif m >= 6 and m <= 8:
            print("Summer")
        elif m >= 9 and m <= 11:
            print("Fall")
        else:
            print("Winter")
    else:
        print(-1)


def check_date(y, m, d):
    if d <= lastDay(y, m):
        return True
    else:
        return False


def check_year(y):
    if y % 4 == 0:
        if y % 100 == 0 and y % 400 != 0:
            return False
        else:
            return True
    else:
        return False


def lastDay(y, m):
    if m == 2:
        if check_year(y):
            return 29
        else:
            return 28
    elif m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    else:
        return 31
    

check_season(Y, M, D)