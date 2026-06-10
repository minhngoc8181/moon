N = int(input())
so_du = N % 9
if so_du == 0:
    print("9" * (N // 9))
else:
    print(str(so_du) * (N // 9 + 1))