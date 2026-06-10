M = int(input())
N = int(input())
so_keo_du = M % N
so_keo = M // N
if so_keo_du == 0:
    print(0)
else:
    print((so_keo + 1) * N - M)