a = 17
b = 5

print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a / b = ", a / b)
print("a // b = ", a // b)
print("a % b = ", a % b)
print("a ** b = ", a ** b)

diem = 6.5
tuoi = 20

diem_kha = diem >= 6.5 and diem < 8.0
print("Điểm đạt loại khá: ", diem_kha)

tuoi_khong_hop_le = tuoi < 18 or tuoi > 60
print("Chưa đủ 18 tuổi hoăc trên 60 tuổi: ", tuoi_khong_hop_le)
print("Tuổi hợp lệ (trong khoảng 18 - 60 tuổi): ", not tuoi_khong_hop_le)