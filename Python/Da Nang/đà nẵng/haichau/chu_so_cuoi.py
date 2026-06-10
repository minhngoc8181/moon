N = int(input())
ans = 1
for i in range(1, N + 1):
    ans *= i

anss = str(ans)
for j in anss[::-1]:
    if j != "0":
        print(j)
        break
