number = int(input())
danh_sach = []
if number % 2 == 0:
    danh_sach.append(2)

if number % 3 == 0:
    danh_sach.append(3)

if number % 5 == 0:
    danh_sach.append(5)

if number % 7 == 0:
    danh_sach.append(7)

chia_het = ", ".join([str(n) for n in danh_sach])
if danh_sach:
    print(f"{number} chia hết cho {chia_het}")
else:
    print(f"{number} không chia hết cho số nào trong các số 2, 3, 5, 7")




"""danh_sach = []

if danh_sach:
    print(danh_sach)

danh_sach.append(2)
danh_sach.append(5)

if danh_sach:
    print(danh_sach)
    print(*danh_sach, sep=", ")
    print(", ".join([str(n) for n in danh_sach]))"""