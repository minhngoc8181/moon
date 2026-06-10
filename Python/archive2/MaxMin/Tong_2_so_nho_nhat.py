A = int(input())
B = int(input())
C = int(input())
D = int(input())
danh_sach = [A, B, C, D]
so_nho_nhat = min(danh_sach)
danh_sach.remove(so_nho_nhat)
so_nho_hai = min(danh_sach)
print(so_nho_nhat + so_nho_hai)