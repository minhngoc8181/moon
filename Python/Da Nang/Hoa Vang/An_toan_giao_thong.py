K = int(input())
S = list("ANTOANGIAOTHONG")
C = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
du1 = K % 15 - 1
du2 = K % 7 - 1
ans1 = S[du1]
ans2 = C[du2]
print(f"{ans1}-{ans2}")