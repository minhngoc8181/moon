a = input()
m = int(input())

text_len = len(a)

dp = [None] * m

for c in a:
    next = dp[:]
    d = int(c)
    for j in range(m):
        if dp[j] is not None:
            print('continue...')
            


