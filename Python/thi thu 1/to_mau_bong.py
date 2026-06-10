N = int(input())
A = int(input())
B = int(input())
count = 0
if N <= 100:
    for i in range(1, N + 1):
        if i % A != 0 and i % B != 0:
            count += 1
    print(count)
else:
    sochihetchoa = N // A
    sochiahetchoB = N // B
    chiahetchoab = N // (A * B)
    print(N - sochiahetchoB - sochihetchoa + chiahetchoab)