S = input()
a = S.count('C')
b = S.count('M')
print(min((a - 1) // 2, b))
