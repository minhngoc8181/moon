A = int(input())
B = int(input())
lon = max(A, B)
be = min(A, B)
if lon == be:
    print(be + be)
else:
    print(be + be + 1)