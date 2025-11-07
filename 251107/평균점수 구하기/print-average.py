grades = list(map(float, input().split()))
avg = sum(grades) / len(grades)
print(f"{avg:.1f}")