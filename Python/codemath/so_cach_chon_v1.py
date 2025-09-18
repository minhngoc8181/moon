# https://laptrinh.codemath.vn/problem/lhpnd20socachchon

n, a, b, c = map(int, input().split())


def choose2(N):
    return N * (N - 1) // 2


def choose3(N):
    return N * (N - 1) * (N - 2) // 6


if n == 3:
    print(a * b * c)
elif n == 4:
    # print((a * b * c * (a + b + c - 3)) // 2)
    print(a * b * choose2(c) + a * choose2(b) * c + choose2(a) * b * c)
elif n == 5:
    print(
        a * b * choose3(c)
        + a * choose2(b) * choose2(c)
        + a * choose3(b) * c
        + choose2(a) * b * choose2(c)
        + choose2(a) * choose2(b) * c
        + choose3(a) * b * c
    )
