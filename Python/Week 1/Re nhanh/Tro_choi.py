X = int(input())
Y = int(input())
so_lon_nhat = max(X, Y)
if X == Y:
    print(X + Y)
elif X > Y:
    print(X + X - 1)
else:
    print(Y + Y - 1)