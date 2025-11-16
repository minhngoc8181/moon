N = int(input())
today = 7
the_next_day = (today + N) % 7
if the_next_day == 1:
    print("CN")
elif the_next_day == 0:
    print(7)
else:
    print(the_next_day)