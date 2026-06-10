'''A = int(input())
B = int(input())
total = 0
for i in range(A, B + 1, 9):
    total += i
    if A % 9 == 0 and B % 9 == 0:
        print(total - (A + B))
    elif A % 9 != 0:
        A = (A // 9) * 9
        print(total - (A + B))
    elif B % 9 != 0:
        B = (A // 9) * 9
        print(total - (A + B))'''

A = int(input())
B = int(input())
first = (A // 9 + 1) * 9
last = (B - 1) // 9 * 9
noftem = (last - first) // 9 + 1
total = (first + last) * noftem // 2
print(total)


A = int(input())
B = int(input())
total = 0
for i in range((A // 9 + 1) * 9, B, 9):
    if i % 9 == 0:
        total += i
print(total)