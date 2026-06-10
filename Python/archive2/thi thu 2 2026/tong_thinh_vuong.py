M = int(input())
N = int(input())
K = int(input())
area = M * N
canhM = M // K 
canhN = N // K
total = canhN * canhM
print(area - total)