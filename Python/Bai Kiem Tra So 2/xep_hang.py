A = int(input())
B = int(input())
if A > B:
    print(B + (B + 1))
elif B > A:
    print(A + (A + 1))
else:
    print(A + B)