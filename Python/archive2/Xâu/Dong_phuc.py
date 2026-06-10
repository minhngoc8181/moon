N = int(input())
sizes = input()
sum = 0
for s in sizes:
    if s == 'S':
        sum += 2
    if s == 'M':
        sum += 3
    if s == 'L':
        sum += 4
print(sum)







'''N = int(input())
A = (N // 3) * (2 + 3 + 4)
B = (N // 3) * (2 + 3 + 4) + 2
C = (N // 3) * (2 + 3 + 4) + 2 + 3
if N % 3 == 0:
    print(A)
elif N % 3 == 1:
    print(B)
else:
    print(C)'''