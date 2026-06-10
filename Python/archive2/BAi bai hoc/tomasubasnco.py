N = int(input())
K = int(input())
total = sum(range(N, 0, -K))
print(total + total - N)
'''start = N
end = N % K
so_so_hang = (start - end) // K + 1
day = (start + end) * so_so_hang // 2
print(day + day - N)'''