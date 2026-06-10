N, M = map(int, input().split())
count = 0
for i in range(1, 100000):
    itext = str(i)
    if len(itext) == M:
        if sum(map(int, itext)) == N:
            count += 1
print(count)