A = int(input())
S = input()
for c in S:
    if c == "L":
        A -= 1
    else:
        A += 1
print(A)