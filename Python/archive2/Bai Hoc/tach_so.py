N = int(input())
if N % 6 == 0:
    print(N // 3 - 2, N // 3, N // 3 + 2)
elif N <= 6:
    print(12 - N)
else:
    print((N // 6 + 1) * 6 - N)