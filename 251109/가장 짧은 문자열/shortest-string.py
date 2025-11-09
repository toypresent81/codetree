a = input()
b = input()
c = input()
if len(a) >= len(b) and len(b) >= len(c):
    print(len(a)-len(c))
elif len(a) >= len(b) and len(c) >= len(b):
    if len(a) >= len(c):
        print(len(a)-len(b))
    else:
        print(len(c)-len(b))
elif len(b) >= len(a) and len(b) >= len(c):
    if len(a) >= len(c):
        print(len(b)-len(c))
    else:
        print(len(b)-len(a))
else:
    print(len(c)-len(a))
