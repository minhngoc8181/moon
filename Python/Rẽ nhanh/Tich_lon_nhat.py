A = int(input())
B = int(input())
C = int(input())
danh_sach = [A, B, C]
so_lon_nhat = max(danh_sach)
danh_sach.remove(so_lon_nhat)
so_lon_hai = max(danh_sach)
if A == 0 or B == 0 or C == 0:
    print(so_lon_nhat * so_lon_hai)
else:
    print(A * B * C)