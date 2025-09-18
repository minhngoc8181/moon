# https://laptrinh.codemath.vn/problem/lhpnd20socachchon

n, a, b, c = map(int, input().split())


def choose(N, R):
    if R > N / 2:
        R = N - R
    ans = 1
    for i in range(1, R + 1):
        ans *= N - R + i
        ans //= i
    return ans


print(
    choose(a + b + c, n)
    - choose(a + b, n)  # include (A&B), A only, B only
    - choose(a + c, n)
    - choose(b + c, n)
    + choose(a, n)
    + choose(b, n)
    + choose(c, n)
)
