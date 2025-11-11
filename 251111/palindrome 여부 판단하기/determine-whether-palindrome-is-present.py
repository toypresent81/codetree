A = input()

def palindrome(a):
    if a[::-1] == a:
        print("Yes")
    else:
        print("No")


palindrome(A)