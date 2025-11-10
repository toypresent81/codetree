A = input()
B = input()

# Please write your code here.
arr_a = list(A)
arr_b = list(B)
while True:
    if B in A:
        for i in range(len(arr_a)):
            if arr_a[i:i+len(arr_b)] == arr_b:
                arr_a = arr_a[:i] + arr_a[i+len(arr_b):]
            A = "".join(arr_a)
    else:
        print("".join(arr_a))
        break
        


    
        
