N = int(input())
thu_tu = N % 6
if thu_tu == 1 or thu_tu == 0:
    print("A")
elif thu_tu == 2 or thu_tu == 5:
    print("B")
else:
    print("C")
