A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
danh_sach = [A, B, C, D, E]
so_lon_nhat = max(danh_sach)
danh_sach.remove(so_lon_nhat)
print(sum(danh_sach))


# print(sum(A, B, C, D, E) - max(A, B, C, D, E))
