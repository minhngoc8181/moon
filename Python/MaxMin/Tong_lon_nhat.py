A = int(input())
B = int(input())
C = int(input())
D = int(input())
danh_sach = [A, B, C, D]
nhat = max(danh_sach)
danh_sach.remove(nhat)
nhi = max(danh_sach)
print(nhat + nhi)