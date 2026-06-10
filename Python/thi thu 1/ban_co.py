N = int(input())
K = int(input())
sodau = N % K
socuoi = N
sohang = N // K + 1
tong = (sodau + socuoi) * sohang // 2
print(tong + tong - N)