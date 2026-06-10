N = int(input())
total = 0
for i in range(1, (N + 1) // 2):
    if N % i == 0:
        total += i + (N // i)
        if total > N:
            print(1)
            break
if total < N:
    print(0)