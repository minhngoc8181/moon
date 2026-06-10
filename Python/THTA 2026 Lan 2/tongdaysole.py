N = int(input())


def cal(K):
    if K == 1:
        return 1
    oddItem = (K + 1) // 2
    return oddItem**2 + cal(K // 2)


print(cal(N))
