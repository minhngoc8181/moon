X = int(input())
is_ok = False
for i in range(9, 1, -1):
    if X % i == 0:
        print(X // i)
        is_ok = True
        break
if is_ok == False:
    print(-1)
