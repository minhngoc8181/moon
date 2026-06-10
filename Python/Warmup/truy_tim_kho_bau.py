N, M, S, T = map(int, input().split())
hang = (S + T - (M - 2 + 1)) // 2 + 1
cot =  S - hang + 2
print(hang, cot)