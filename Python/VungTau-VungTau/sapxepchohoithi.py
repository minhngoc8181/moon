N = int(input())
if N % 3 == 0:
    print(N // 3)
    print(0)
elif N % 3 == 2:
    print(N // 3)
    print(N % 3 // 2)
else:
    print(N // 3 - 1)
    print(N % 3 + 1)