N = int(input())
count = 0
for i in range(0, 100000000):
    inText = str(i)
    totaldigit = sum(map(int, inText))
    if (totaldigit + i) % 10 == 0:
        count += 1
        if count == N:
            print(i)
            break