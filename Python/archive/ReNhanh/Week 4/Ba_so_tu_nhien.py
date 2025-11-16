A = int(input())
B = int(input())
C = int(input())
nhat = max(A, B, C)
tong = (A + B + C) - max(A, B, C)
if tong == nhat:
    print("YES")
else:
    print("NO")