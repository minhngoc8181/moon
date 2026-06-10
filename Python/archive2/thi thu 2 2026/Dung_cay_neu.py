N = int(input())
if N <= 3:
    print(2)
elif N % 5 == 0:
    print(N // 5 * 3)
elif N % 5 == 1:
    print(N // 5 * 3 + 1)
elif N % 5 == 2:
    print(N // 5 * 3 + 2)
elif N % 5 == 3:
    print(N // 5 * 3 + 2)
else:
    print(N // 5 * 3 + 3)