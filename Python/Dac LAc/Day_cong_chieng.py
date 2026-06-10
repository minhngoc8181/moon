N = int(input())
day = []
for i in range(2, N + 1):
    if i % 2 == 0 or i % 5 == 0:
        day.append(i)
print(* day)