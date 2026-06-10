N = int(input())
x = int(input())
y = int(input())

start, end = y, y + N * (N - 1)
total = (start + end) * N // 2

# 0*N+1, 2*N+1, 4*N+1.......                            , 1*N+1
# (1-1)  (2-1)  (3-1)

if x <= (N + 1) // 2:
    start = 2 * (x - 1) * N + 1
else:
    x = N - x
    start = (2 * x + 1) * N + 1

end = start + N - 1
total += (start + end) * N // 2

total -= start + y - 1

print(total % 2026)
