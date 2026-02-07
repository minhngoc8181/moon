N = int(input())
count = 0
divi = []
for i in range(2, N):
    if (N // i) == (N % i):
        count += 1
        divi.append(i)
print(count,end='')
print(':', end='')
print(*divi)