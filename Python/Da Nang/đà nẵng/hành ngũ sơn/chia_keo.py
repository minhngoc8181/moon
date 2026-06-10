N = int(input())
candy = list(map(int, input().split()))
candy.sort()
hop = 1
for i in range(1, len(candy)):
    if candy[i] - candy[i-1] == 1:
        hop = 2
        break
print(hop)