H = int(input())
M = int(input())
K = int(input())
count = 0
for i in range(0, K + 1):
    if sum(map(int, str(H))) == sum(map(int, str(M))):
        count += 1
    M += 1
    if M == 60:
        M = 0
        H += 1
    if H == 24:
        H = 0
print(count)