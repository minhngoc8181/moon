N = int(input())
if N % 2 != 0:
    print((1 + (N - 2)) * (N // 2) // 2)
else:
    print((1 + (N - 1)) * (N // 2) // 2)
    
N = int(input())   
nofitem = N // 2
print(nofitem * nofitem)