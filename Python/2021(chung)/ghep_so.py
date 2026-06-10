A = input()
B = input()
A, B = min(A, B), max(A, B)
lenA = len(A)
totalA = sum(map(int, A))
lenB = len(B)
totalB = sum(map(int, B))

minDA = 1000
minDB = 1000
for i in range(1, 100):
    for j in range(1, 100):
        if (i * totalA + j * totalB) % 9 == 0:
            if i * lenA + j * lenB <= minDA + minDB:
                minDA = i
                minDB = j

print(A * minDA + B * minDB)
