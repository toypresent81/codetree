N = int(input())
cnti = 0
cntj = 0
for i in range(N):
    cnti = (i+1)*N
    for j in range(N):   
        cntj += 1          
        if i % 2 == 0:              
            print(cntj, end=" ")
        else:                  
            print(cnti, end=" ")
            cnti -= 1      
    print()