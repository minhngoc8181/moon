K = int(input())
N = int(input())
total = 0
count = 0
for i in range(1, N + 1):
    for j in range(K):
        print(i)
        if count <  N:
            total += i 
        count += 1
        
print(total)