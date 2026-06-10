A, B, C, D, K = list(map(int,input().split()))
count = 0
for i in range(A, B + 1):
    for j in range(C, D + 1):
        if (i + j) % K == 0:
            count += 1
print(count)