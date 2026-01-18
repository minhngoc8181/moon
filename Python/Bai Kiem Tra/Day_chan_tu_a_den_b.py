A = int(input())
B = int(input())
total = 0
for i in range(A, B + 1 , 2):
    if i % 2 == 0:
        total += i
print(total)