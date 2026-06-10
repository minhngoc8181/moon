A = int(input())
B = int(input())
C = int(input())
so_nho_nhat = min(A, B, C)
so_lon_nhat = max(A, B, C)
tong = so_nho_nhat + so_lon_nhat
tich = so_nho_nhat * so_lon_nhat
print(tich % tong)