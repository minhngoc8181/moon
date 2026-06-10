H = int(input())
M = int(input())
K = int(input())

count = 0
for i in range(0, K + 1):
    if M >= 60:
        H += 1
        M -= 60
    if H >= 24:
        H -= 24

    if sum(map(int, str(H))) == sum(map(int, str(M))):
        count += 1
        
    M += 1

print(count)
