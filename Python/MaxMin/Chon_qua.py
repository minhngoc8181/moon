A = int(input())
B = int(input())
C = int(input())
danh_sach = [A + B, A + C, B + C]
danh_sach.sort()

if danh_sach[2] % 2 == 0:
    print(danh_sach[2])
elif danh_sach[1] % 2 == 0:
    print(danh_sach[1])
else:
    print(danh_sach[0])


danh_sach = [A, B, C]
danh_sach.sort()
if (danh_sach[2] + danh_sach[1]) % 2 == 0:
    print(danh_sach[2] + danh_sach[1])
elif (danh_sach[2] + danh_sach[0]) % 2 == 0:
    print(danh_sach[2] + danh_sach[0])
else:
    print(danh_sach[0] + danh_sach[1])