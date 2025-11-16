N = int(input())
A = int(input())
B = int(input())
M = N * N
Aa = A * B // 2
C = (N - B) * N // 2
B = (N - A) * N // 2
T = Aa + B + C
D = M - T
print(D)