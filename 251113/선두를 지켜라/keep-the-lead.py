n, m = map(int, input().split())

MAX_RANGE = 1000000
ans_a = [0] * (MAX_RANGE + 1)
ans_b = [0] * (MAX_RANGE + 1)

time_a, time_b = 1, 1
for _ in range(n):
    velocity, time = map(int, input().split())
    for i in range(time):
        ans_a[time_a] = ans_a[time_a - 1] + velocity
        time_a += 1
        
for _ in range(m):
    velocity, time = map(int, input().split())
    for i in range(time):
        ans_b[time_b] = ans_b[time_b - 1] + velocity
        time_b += 1

count = 0
leader = 0  

for i in range(1, min(time_a, time_b)):
    if ans_a[i] > ans_b[i]:
        current_leader = 1  
    elif ans_a[i] < ans_b[i]:
        current_leader = 2 
    else:
        current_leader = 0  
    
    if leader != 0 and current_leader != 0 and leader != current_leader:
        count += 1
    
    if current_leader != 0:
        leader = current_leader

print(count)