money = int(input())
denominations = [500000, 200000, 100000, 50000, 20000, 10000, 5000, 2000, 1000]
# Tính số tờ tiền cho từng mệnh giá

ah_1 = money // 500000
if ah_1 >= 1:
    print(f"{ah_1} tờ 500000")
money = money % 500000

ah_2 =  money // 200000
if ah_2 >= 1:
    print(f"{ah_2} tờ 200000")
money = money % 200000

ah_3 = money // 100000
if ah_3 >= 1:
    print(f"{ah_3} tờ 100000")
money = money % 100000

ah_4 = money // 50000
if ah_4 >= 1:
    print(f"{ah_4} tờ 50000")
money = money % 50000

ah_5 = money // 20000
if ah_5 >= 1:
    print(f"{ah_5} tờ 20000")
money = money % 20000

ah_6 = money // 10000
if ah_6 >= 1:
    print(f"{ah_6} tờ 10000")
money = money % 10000

ah_7 = money // 5000
if ah_7 >= 1:
    print(f"{ah_7} tờ 5000")
money = money % 5000

ah_8 = money // 2000
if ah_8 >= 1:
    print(f"{ah_8} tờ 2000")
money = money % 2000

ah_9 = money // 1000
if ah_9 >= 1:
    print(f"{ah_9} tờ 1000")
