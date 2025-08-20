N = int(input())
# in every 60 number, there are 60 - (15+12+10-3-2-1+1) = 32 numbers which is not divided by 4, 5, 6.
M = (N // 32) * 60
count = M / 60 * 32
for i in range(M + 1, M + 60):
    if i % 4 != 0 and i % 5 != 0 and i % 6 != 0:
        count += 1
        if count == N:
            print(i)
            break
