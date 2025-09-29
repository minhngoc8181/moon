N = int(input())
X = int(input())
Y = int(input())
total = X + Y
days = (N + total - 1) // total
# 9 // 9 = 15 // 9 = 17 // 9
# (15 + 9 - 1) // 9 = 
print(days)


"""import math

N = int(input())
X = int(input()) 
Y = int(input())
total = X + Y
days = math.ceil(N / total)
print(days)"""


"""if N % total == 0:
    print(days)
else:
    print(days + 1)"""
