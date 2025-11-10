string = input()
countEE = 0
countEB = 0
for i in range(len(string)-1):
    if string[i] + string[i+1] == "ee":
        countEE += 1
    if string[i] + string[i+1] == "eb":
        countEB += 1
    
print(countEE, countEB)