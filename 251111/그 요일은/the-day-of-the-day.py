m1, d1, m2, d2 = map(int, input().split())
A = input()

def nums_of_days(m, d):

    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_of_days = 0

    for i in range(1, m):
        total_of_days += days[i]
    total_of_days += d
    return total_of_days

diff_days = nums_of_days(m2, d2) - nums_of_days(m1, d1)

week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print(diff_days//7 + 1)

