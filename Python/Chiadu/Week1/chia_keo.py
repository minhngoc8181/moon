N = int(input())
M = int(input())
last_person = M % N
if M % N != 0:
    print(last_person)
else:
    print(N)