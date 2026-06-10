N = int(input())
chia_het_cho_2 = N // 2
chia_het_cho_6 = N // 6
print(chia_het_cho_2 - chia_het_cho_6)
"""count = 0
for i in range(1, N + 1):
    if i % 3 != 0 and i % 2 == 0:
        count += 1
print(count)"""

# (2 + (N - (N % 2))) * N - (N % 2) // 2 // 2