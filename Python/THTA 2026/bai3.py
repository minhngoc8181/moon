N = int(input())
if N <= 10:
    ans = [0, 1, 2, 3, 6, 9, 12, 17]
    print(ans[N])
else:
    s1 = N
    if N % 3 == 0:
        e1 = 3
    else:
        e1 = N % 3

    if N == 3:
        ssh = 1
    elif N % 3 == 0:
        ssh = N // 3
    elif N == 5:
        ssh = 2
    elif N == 7:
        ssh = N // 3 + 2
    else:
        ssh = N % 3 + 1

    tong = (s1 + e1) * ssh // 2
    # print(tong, s1, e1, ssh)
    print(tong + tong - N)