K = int(input()) # số dòng trong 1 trang
N = int(input()) 
X = 0
if N % K != 0:
    X = N // K + 1
else:
    X = N // K
Y = N - K * ( X - 1)
print(X, Y)
