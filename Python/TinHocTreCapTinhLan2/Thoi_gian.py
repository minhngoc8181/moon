T = int(input())
thoi_gian_1 = 8 + (T // 60)
thoi_gian_2 = T % 60


if 9 < T < 60:
    print(f"08:{T}")
elif T <= 9:
    print(f"08:0{T}")
elif T // 60 == 1 and T % 60 <= 9:
    print(f"0{thoi_gian_1}:0{thoi_gian_2}")
elif T // 60 == 1:
    print(f"0{thoi_gian_1}:{thoi_gian_2}")
elif T // 60 != 1 and T % 60 <= 9:
    print(f"{thoi_gian_1}:0{thoi_gian_2}")
else:
    print(f"{thoi_gian_1}:{thoi_gian_2}")