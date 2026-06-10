N = int(input())
A = int(input())
B = int(input())
count = 0
if N < 1000000:
    for i in range(1, N + 1):
        if i % A != 0 and i % B != 0:
            count += 1
    print(count)
else:
    khac = N // A + N // B - N // A // B
    print(N - khac)