N = int(input())
a = int(input())
b = int(input())
x = int(input())
y = int(input())

if a != x and b != y:
    print(4 * N - 4)
elif a != x or b != y:
    print(3 * N - 2)
else:
    print(2 * N - 1)
