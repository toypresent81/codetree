s, q = input().split()
for i in range(int(q)):
    a, b, c = input().split()
    if int(a) == 1:
        s_arr = list(s)
        b1 = s_arr[int(b)-1]
        c1 = s_arr[int(c)-1]
        s_arr[int(b)-1] = c1
        s_arr[int(c)-1] = b1
        s = "".join(s_arr)
    else:
        s = s.replace(b, c)
    print(s)


