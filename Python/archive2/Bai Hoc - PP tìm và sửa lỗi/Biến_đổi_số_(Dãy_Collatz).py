N = int(input())
for i in range(0, 10000000):
    if N == 1:
        print(i)
        break
    else:
        if N % 2 == 0:
            N //= 2
        else:
            N = N * 3 + 1