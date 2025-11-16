N = int(input())
if N <= 10:
    print(20_000 * N)
elif N <= 50:
    print(200_000 + 18_000 * (N - 10))
else:
    print(920_000 + 15_000 * (N - 50))