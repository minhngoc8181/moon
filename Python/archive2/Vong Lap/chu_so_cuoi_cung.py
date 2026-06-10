N = int(input())
tich = 0
for i in range(1, N + 1):
    tich *= i
if tich % 10 == 0:
    print(i % 100)