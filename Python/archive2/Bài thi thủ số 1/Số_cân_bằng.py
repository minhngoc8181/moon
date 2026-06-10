N = int(input())
S = str(N)
dight = len(S)
if dight % 2 == 0:
    hafl = dight // 2
    a = S[:hafl]
    b = S[hafl:]
    if a == b:
        print("Yes")
    else:
        print("No")
else:
    print("No")