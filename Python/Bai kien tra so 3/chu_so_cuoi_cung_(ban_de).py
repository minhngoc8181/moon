N = int(input())
nhan = 1
for i in range(1, N + 1):
    nhan *= i
if nhan % 1000 == 0:
    print(nhan // 1000 % 10)
elif nhan % 100 == 0:
    print(nhan // 100 % 10)
elif nhan % 10 == 0:
    print(nhan // 10 % 10)