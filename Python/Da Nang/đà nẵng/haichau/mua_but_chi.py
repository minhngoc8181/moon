N = int(input())
print((N // 9 * 20) + (N % 9 // 4 * 10) + ((N % 9 % 4) * 3))