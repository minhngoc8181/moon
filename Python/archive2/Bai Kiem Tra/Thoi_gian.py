"""T = int(input())
tieng = T // 60
phut = T % 60
end_tieng = 8 + tieng
end_phut = 00 + phut
if tieng == 0 and phut < 10:
    print(f"0{end_tieng}:0{end_phut}")
elif phut < 10:
    print(f"{end_tieng}:0{end_phut}")
elif tieng == 0:
     print(f"0{end_tieng}:{end_phut}")
else:
    print(f"{end_tieng}:{end_phut}")"""   

T = int(input())
tieng = T // 60
phut = T % 60
print(f"{tieng+8:02}:{phut:02}")