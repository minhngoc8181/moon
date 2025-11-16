x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
A1 = 0
A2 = 0
A3 = 0
if x1 > y1:
    A1 += 3
elif x1 < y1:
    A2 += 3
else:
    A2 += 1
    A1 += 1

if x2 > y2:
    A1 += 3
elif x2 < y2:
    A3 += 3
else:
    A3 += 1
    A1 += 1
  
if x3 > y3:
    A2 += 3
elif x3 < y3:
    A3 += 3
else:
    A2 += 1
    A3 += 1

nhat = max(A1, A2, A3)
if A1 == nhat:
    print(f"A1 {nhat}")
elif A2 == nhat:
    print(f"A2 {nhat}") 
else:
    print(f"A3 {nhat}") 