A = int(input())
B = int(input())
C = int(input())
D = int(input())
if A - B == 1 and B - C == 1 and C - D == 1:
    print("DOWN")
elif D - C == 1 and C - B == 1 and B - A == 1:
    print("UP")
elif A == B and B == C and C == D:
    print("EQUAL")
else:
    print("NONE")