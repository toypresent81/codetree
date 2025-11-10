string = input()
for i in string:
    if i.isalpha() == True or i.isdigit() == True:
        if i.isalpha() == True:
            print(i.lower(), end="" )
        else:
            print(i, end="")