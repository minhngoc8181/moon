# https://laptrinh.codemath.vn/problem/lhp18muasach
import math

X, Y = map(int, input().split())
Z = 3

ans1 = math.comb(X + Y + Z, 3)
ans2 = math.comb(X, 4) * math.comb(Y, 4) * math.comb(Z, 2)
ans3 = (
    math.comb(X + Y, 4)
    + math.comb(X + Z, 4)
    + math.comb(Y + Z, 4)
    - 2 * math.comb(X, 4)
    - 2 * math.comb(Y, 4)
)
ans4 = (
    math.comb(X + Y, 4)
    + math.comb(X + Z, 4)
    + math.comb(Y + Z, 4)
    - math.comb(X, 4)
    - math.comb(Y, 4)
)

print(ans1, ans2, ans3, ans4)
