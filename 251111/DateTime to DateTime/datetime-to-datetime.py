a, b, c = map(int, input().split())

def num_of_days(m, d):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0
    
    for i in range(1, m):
        total_days += days[i]
    total_days += d
    
    return total_days    

def num_of_times(h, m):
    return 60 * h + m

total_days = num_of_days(11, a) - num_of_days(11, 11)
total_minutes = 24 * 60 * total_days + num_of_times(b, c) - num_of_times(11, 11)
print(total_minutes)