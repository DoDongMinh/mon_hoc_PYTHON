# Bài tập 5.1 - Toán tử số học
a = 17
b = 5

print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a / b = ", a / b)
print("a // b = ", a // b)
print("a % b = ", a % b)
print("a ** b = ", a ** b)

# Bài tập 5.2 - Toán tử so sánh & logic
diem = 6.5
tuoi = 20

diem_kha = diem >= 6.5 and diem < 8.0
print("Điểm đạt loại khá: ", diem_kha)
tuoi_khong_hop_le = tuoi < 18 or tuoi > 60
print("Chưa đủ 18 tuổi hoăc trên 60 tuổi: ", tuoi_khong_hop_le)
print("Tuổi hợp lệ (trong khoảng 18 - 60 tuổi): ", not tuoi_khong_hop_le)

# Bài tập 5.3 - Toán tử gán & toán tử đặc biệt
x = 10
x += 5;  print("x sau += 5:", x)   
x -= 3;  print("x sau -= 3:", x)   
x *= 2;  print("x sau *= 2:", x)   
x /= 4;  print("x sau /= 4:", x)   
x //= 2; print("x sau //= 2:", x) 
x **= 3; print("x sau **= 3:", x) 

danh_sach = [1, 2, 3, "python"]
print("3 có trong danh_sach không?:", 3 in danh_sach) 

list_a = [1, 2, 3]
list_b = list_a          
list_c = [1, 2, 3]       

print("list_a is list_b:", list_a is list_b)  
print("list_a is list_c:", list_a is list_c)  

# Bài tập 5.4 - Độ ưu tiên toán tử
ket_qua_1 = 2 + 3 * 4 ** 2
print("Kết quả 1:", ket_qua_1)  
ket_qua_2 = (2 + 3) * 4 ** 2
print("Kết quả 2:", ket_qua_2)  
ket_qua_3 = 10 > 5 and 3 < 1 or not False
print("Kết quả 3:", ket_qua_3)  