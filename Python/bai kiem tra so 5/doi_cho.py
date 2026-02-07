N = int(input())
for i in range(N):
    chuoi = input()
    if chuoi == "abc":
        print(0)
    elif chuoi == "acb":
        print(1)
    elif chuoi == "bac":
        print(1)
    elif chuoi == "bca":
        print(0) 
    elif chuoi == "cab":
        print(0)
    else:
        print(1)

