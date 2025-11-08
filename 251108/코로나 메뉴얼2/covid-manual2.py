hospi = [0 for _ in range(4)]
for i in range(3):
    arr = input().split()
    a = arr[0]
    b = int(arr[1])
    if a == "Y" and b >= 37:
        hospi[0] += 1
    elif a == "N" and b >= 37:
        hospi[1] += 1
    elif a == "Y" and b < 37:
        hospi[2] += 1
    else:
        hospi[3] += 1

for i in range(4):    
    print(hospi[i], end=" ")        

if hospi[0] >= 2:
    print("E", end=" ")
  
