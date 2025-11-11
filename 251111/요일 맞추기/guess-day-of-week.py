m1, d1, m2, d2 = map(int, input().split())

def nums_of_days(m, d):

    total_of_days = 0
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(1, m):
        total_of_days += days[i]

    total_of_days += d
    return total_of_days

total_of_days = nums_of_days(m2, d2) - nums_of_days(m1, d1)

def check_week(d):
    week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    return week[d % 7]

print(check_week(total_of_days))





