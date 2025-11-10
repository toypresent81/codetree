A = input()
total = 0
for i in A:
    if i.isdigit() == True:
        total += int(i)
print(total)