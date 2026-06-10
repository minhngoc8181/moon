N = int(input())
if N < 25:
    print(N // 7)
elif N < 285:
    print((N // 25 * 4) + (N % 25 // 7))
else:
    print((N // 285 * 48) + (N % 285 // 25 * 4) + (N % 285 % 25 // 7))