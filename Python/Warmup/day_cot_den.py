# import math
N, K = map(int, input().split())
a = N - 1
b = 1 + K * (N - 1)
# d = math.gcd(a, b)
print(f"{a}/{b}")