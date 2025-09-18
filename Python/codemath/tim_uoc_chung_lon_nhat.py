# https://laptrinh.codemath.vn/problem/timuocchunglonnhat

import math

N = int(input())
numbers = list(map(int, input().split()))

max_gcd = 1
for i in range(N):
    for j in range(i + 1, N):
        max_gcd = max(max_gcd, math.gcd(numbers[i], numbers[j]))
print(max_gcd)
