A = int(input())
B = int(input())
C = int(input())
D = int(input())
danh_sach = [A, B, C, D]
so_lon_nhat = max(danh_sach)
danh_sach.remove(so_lon_nhat)
so_lon_hai = max(danh_sach)
print(so_lon_hai + so_lon_nhat + 1)