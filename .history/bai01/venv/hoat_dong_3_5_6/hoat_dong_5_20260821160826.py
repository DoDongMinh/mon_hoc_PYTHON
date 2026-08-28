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

x = 10

x += 5;  print("x sau += 5:", x)   # 15  (10 + 5)
x -= 3;  print("x sau -= 3:", x)   # 12  (15 - 3)
x *= 2;  print("x sau *= 2:", x)   # 24  (12 * 2)
x /= 4;  print("x sau /= 4:", x)   # 6.0 (24 / 4)
x //= 2; print("x sau //= 2:", x) # 3.0 (6.0 // 2)
x **= 3; print("x sau **= 3:", x) # 27.0 (3.0 ** 3)

danh_sach = [1, 2, 3, "python"]
print("3 có trong danh_sach không?:", 3 in danh_sach)  # Output: True

list_a = [1, 2, 3]
list_b = list_a          
list_c = [1, 2, 3]       

print("list_a is list_b:", list_a is list_b)  
print("list_a is list_c:", list_a is list_c)  