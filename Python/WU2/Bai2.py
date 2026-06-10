n, m, S, T = map(int, input().split())
hang = 1 + (S + T - (m - 1)) //2
cot = S - hang + 2
print(hang, cot)