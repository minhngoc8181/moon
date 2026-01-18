A = int(input())
B = int(input())
total = 0
A = A + A % 2
B = B - B % 2
no_of_item = (B - A) // 2 + 1
total = (A + B) * no_of_item // 2
print(total)