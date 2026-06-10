N = int(input())
M = int(input())
if N <= 1000000:
    day = []
    for i in range(1, N + 1):
        if i % 3 == 1:
            day.append(i)
    for j in range(2, N + 1):
        if j % 3 == 2:
            day.append(j)
    for n in range(3, N + 1, 3):
        if n % 3 == 0:
            day.append(n)
    print(day[M - 1])
else:
    mod1 = (N + 2) // 3
    mod2 = (N + 1) // 3
    mod3 = N // 3
    if M <= mod1:
        print(1 + 3 * (M - 1))
    elif M <= mod1 + mod2:
        print(2 + 3 * (M - mod1 - 1))
    else:
        print(3 + 3 * (M - mod2 - mod1 - 1))