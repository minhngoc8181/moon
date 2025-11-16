A = int(input())
B = int(input())
C = int(input())
danh_sach = [A, B, C]
nhat = min(danh_sach)
danh_sach.remove(nhat)
nhi = min(danh_sach)
print(f"{nhat}{nhi}")