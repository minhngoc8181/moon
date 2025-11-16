n = int(input())
table = [[0] * n for i in range(n)]

if n % 2 == 0:
    for i in range(n // 2):
        table[i][i] = 1
        table[i][n - 1 - i] = 2
        table[n - 1 - i][n - 1 - i] = 1
        table[n - 1 - i][i] = 2
else:
    for i in range(n // 2 - 1):
        table[i][i] = 1
        table[i][n - 1 - i] = 2
        table[n - 1 - i][n - 1 - i] = 1
        table[n - 1 - i][i] = 2
    i = n // 2 - 1
    table[i][i] = 1
    table[i][i + 1] = 2
    table[i + 1][i] = 2
    i = n - 1 - i
    table[i][i] = 2
    table[i - 1][i] = 1
    table[i][i - 1] = 1

for row in table:
    print(*row)
