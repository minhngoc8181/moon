N = int(input())
num = list(range(1, N + 1))
for i in range(1, N):
    for j in range(0, N - 1):
     num[j] = (num[j] + num[j + 1]) % 10 ** 9
print(num[0])

"""ans = [0, 1, 3, 8, 20, 48, 112, 256]
print(ans[N])"""