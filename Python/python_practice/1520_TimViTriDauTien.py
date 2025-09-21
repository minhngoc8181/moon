"""
5
1 3 5 7 5 9 5

10
1 2 3 4 5 6 7 8 9
"""



M = int(input())

number = list(map(int, input().split()))
found = False
for position in range(len(number)):
    if number[position] == M:
        print(position)
        found = True
        break
if found == False:
    print(-1)