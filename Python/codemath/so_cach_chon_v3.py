# https://laptrinh.codemath.vn/problem/lhpnd20socachchon

import math

n, a, b, c = map(int, input().split())

print(
    math.comb(a + b + c, n)
    - math.comb(a + b, n)  # include (A&B), A only, B only
    - math.comb(a + c, n)
    - math.comb(b + c, n)
    + math.comb(a, n)
    + math.comb(b, n)
    + math.comb(c, n)
)
