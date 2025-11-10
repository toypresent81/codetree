for i in range(10):
    string = input()
    if string == "END":
        break
    string = string[::-1]
    print(string)