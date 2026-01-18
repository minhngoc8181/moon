N = int(input())
a = int(input())
b = int(input())
yellow = 0
if N <= 100:
    for i in range(1, N + 1):
        if i % a != 0 and i % b != 0:
            yellow += 1
    print(yellow)
else:
    red = N // a
    green = N // b
    yellow = N - red - green + N // (a * b)
    print(yellow)