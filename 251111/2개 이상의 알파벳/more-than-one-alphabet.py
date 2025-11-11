A = input()
empty_arr = [0 for _ in range(26)]

def two_more_alpha(a):

    is_two_more = False
    for i in range(len(a)):
        count = 0
        for j in range(1, len(a)- 1):
            if a[i] != a[j]:
                count += 1
        
        if count >= 2:
            is_two_more = True
            break
    return is_two_more


print("Yes" if two_more_alpha(A) else "No")


    