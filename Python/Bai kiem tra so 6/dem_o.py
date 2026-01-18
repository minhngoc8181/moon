N = int(input())
X1 = int(input())
Y1 = int(input())
X2 = int(input())
Y2 = int(input())
rong = Y2 - Y1 + 1
dai = X2 - X1 + 1
dien_tich = rong * dai

if (X1 + Y1) % 2 == 0:
    print((dien_tich + 1) // 2)
    print(dien_tich // 2)
else:
    print(dien_tich // 2)
    print((dien_tich + 1) // 2)
