X = int(input())
Y = int(input())
Z = int(input())
distance_C_A = abs(Z-X)
distance_C_B = abs(Z-Y)
if distance_C_A < distance_C_B:
    print(distance_C_A)
else:
    print(distance_C_B)