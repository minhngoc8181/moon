N = int(input())
tong = (1 + N - 1) * (N - 1) // 2
tong_5 = 5 + (N // 5 * 5) * (N // 5) // 2
if N // 8 == 0:
    O = N
elif N // 8 * 8 + 3 < N:
    O = N // 8 * 8 + 3
else:
    O = N // 8 * 8
tong_5_3 = (8 + O) * (O // 8) // 2
print(tong, tong_5, tong_5_3)
print(tong - tong_5 - tong_5_3)