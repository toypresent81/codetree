string = input()
a = int(input())
if len(string) < a:
    print(string)
else:
    for i in range(len(string)-1, len(string)-1-a, -1):
        print(string[i], end="")
