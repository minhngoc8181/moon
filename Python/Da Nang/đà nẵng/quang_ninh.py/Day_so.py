N = int(input())
if N % 5 == 2:
    tong1 = (2 + N) * (N // 5 + 1) // 2
    tong2 = (3 + (N - 4)) * ((N - 4) // 5 + 1) // 2
    print(tong1 + tong2)
elif N % 5  == 3:
    tong1 = (2 + N - 1) * ((N - 1) // 5 + 1) // 2
    tong2 = (3 + N) * (N // 5 + 1) // 2
    print(tong1 + tong2)
elif N % 5 == 0:
    print((N + 2) % 10)
elif N % 5 == 1:
    print((N + 1) % 10)
else:
    print((N + 3) % 10)