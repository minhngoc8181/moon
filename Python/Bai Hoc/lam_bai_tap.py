A = int(input())
B = int(input())
C = int(input())
D = int(input())
both_start = max(A, C)
both_end = min(B, D)
if both_start < both_end:
    print(both_end - both_start)
else:
    print(0)