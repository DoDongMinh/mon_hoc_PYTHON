# Bài tập 6.1
bien = 10
print(bien, type(bien))

bien = "Xin chao"
print(bien, type(bien))

bien = 3.14
print(bien, type(bien))

bien = True
print(bien, type(bien))

# Bài tập 6.2
ho_ten = "Nguyen Van A"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0

dtb = (diem_toan + diem_ly + diem_hoa) / 3

loai_gioi = dtb >= 8.0
loai_kha = dtb >= 6.5 and dtb < 8.0
loai_trung_binh = dtb >= 5.0 and dtb < 6.5
loai_yeu = dtb < 5.0

print(ho_ten, "- Điểm trung bình:", round(dtb, 2))
print("Đạt loại giỏi", loai_gioi)
print("Đạt loại khá", loai_kha)
print("Đạt loại trung bình", loai_trung_binh)
print("Đạt loại yếu", loai_yeu)
print("Kiểu dữ liệu của loai_gioi: ", type(loai_gioi))