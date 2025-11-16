P = int(input())
Q = int(input())
R = int(input())
S = int(input())
U = int(input())
V = int(input())
A, B, C = 0, 0, 0
if P > Q:
    A += 3
elif Q > P:
    B += 3
else:
    A += 1
    B += 1
    
if R > S:
    A += 3
elif S > R:
    C += 3
else:
    A += 1
    C += 1
    
if U > V:
    B += 3
elif V > U:
    C += 3
else:
    B += 1
    C += 1

print(A)
print(B)
print(C)