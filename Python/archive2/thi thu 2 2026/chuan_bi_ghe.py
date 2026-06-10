A = int(input())
B = int(input())
if A % 2 == 0:
    if B % 2 == 0:
        print((A + B) // 2)
    else:
        print(A // 2 + B // 2 + 1)
else:
    if B % 2 == 0:
        print(A // 2 + 1 + B // 2)
    else:
        print(A // 2 + 1 + B // 2 + 1)