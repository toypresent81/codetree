string = input()
l = len(string)

print(string)
for i in range(l):
    string = string[-1] + string[:-1]
    print(string)