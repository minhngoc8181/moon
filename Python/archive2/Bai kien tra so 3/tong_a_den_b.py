A = int(input())
B = int(input())
total = 0
for i in range(B + 1):
    number = i * i + 1
    if A <= number <= B:
        total += number
    elif number > B:
        break
print(total)