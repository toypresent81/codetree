m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
num_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

from_month_total = d1 + 1
for i in num_of_days[:m1]:
    from_month_total += i

to_month_total = d2 + 1
for i in num_of_days[:m2]:
    to_month_total += i

print(to_month_total- from_month_total)
