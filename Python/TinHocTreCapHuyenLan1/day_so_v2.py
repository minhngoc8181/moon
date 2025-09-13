n = int(input())
count = 0
for i in range(1, n + 1):
    num = (1 + i) * i // 2
    print(i, num, i % 6, num % 6, sep="\t")

print(count)
