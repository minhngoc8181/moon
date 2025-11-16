N = int(input())
found = False
for i in range(1, N + 1):
    if i * i != N :
        print("Sai")
        found = True
        break
if found == True:
    print("Đúng")