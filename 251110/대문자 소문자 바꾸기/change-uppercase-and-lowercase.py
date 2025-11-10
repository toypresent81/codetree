string = input()
for i in string:
    if i >= "A" and i <= "Z":
        print(i.lower(), end="")
    else:
        print(i.upper(), end="")