AM, AE = map(int, input().split())
BM, BE = map(int, input().split())
if AM > BM: 
    print("A")
elif AM == BM:
    if AE > BE:
        print("A")
    else:
        print("B")
else:
    print("B")