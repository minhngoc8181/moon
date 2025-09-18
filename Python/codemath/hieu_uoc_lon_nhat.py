# https://laptrinh.codemath.vn/problem/lhp18usln

import math

N = int(input())

limit = math.floor(math.sqrt(N))
maxFactor = 1
for factor in range(2, limit + 1):
    if N % factor == 0:
        maxFactor = N // factor
        break
    
print(N - maxFactor)
