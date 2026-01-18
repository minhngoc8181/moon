N = int(input())
for i in range(1, N + 1):
    if i * i == N:
        print(1)
        break
    elif i * i > N:
        print(0)
        break