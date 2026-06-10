K = int(input())
A = int(input())
B = int(input())

O1 = (K // A )* A
if O1 + B <= K:
    O1 += B

O3 = B + ((K - B) // A * A)

O2 = (K // B) * B
if O2 + A <= K:
    O2 += A

O4 = A + ((K - A) // B * B)

print(max(O1, O2, O3, O4))