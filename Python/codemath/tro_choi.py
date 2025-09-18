# https://laptrinh.codemath.vn/problem/trochoi_vung_tau_2223

N, K = map(int, input().split())
energies = list(map(int, input().split()))

minValues = [100_000_000_0000] * N
minValues[0] = 0

for i in range(N):
    for j in range(i + 1, min(i + K + 1, N)):
        minValues[j] = min(minValues[j], minValues[i] + abs(energies[i] - energies[j]))

print(minValues[-1])
