P = int(input())
N = int(input())
K = int(input())
total = 0
for i in range(1, N + 1):
    total += i * K
if total <= P:
    print("YES")
else:
    print(total - P)
    
# total = (1 * K + N * K) * N // 2
