A = int(input())
B = int(input())
C = int(input())
D = int(input())
digits = [A,B,C,D]
count = 0
for i in range(len(digits)):
    for j in range(i+1, len(digits)):
        if (digits[i] + digits[j]) % 3 == 0:
            if digits[i] != 0:
                count += 1
            if digits[j] != 0:
                count += 1
print(count)