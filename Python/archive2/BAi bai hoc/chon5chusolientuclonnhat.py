S = input()
maxvalue = 0
for i in range(0, len(S)):
    d = int(S[i : i + 5])
    if d > maxvalue:
        maxvalue = d
print(maxvalue)


"""S = input()
maxValue = 0
for i in range(0, len(S)-4):
    d = int(S[i : i + 5])
    if d > maxValue:
        maxValue = d
print(maxValue)"""