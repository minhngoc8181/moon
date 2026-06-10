N = int(input())
if N % 2 == 0:
    for i in range(N - 2, 0, -2):
        print(i)
else:
    for j in range(N - 1, 0, -2):
        print(j)