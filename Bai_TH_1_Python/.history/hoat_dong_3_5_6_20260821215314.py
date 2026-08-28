#hoat dong 3.1: soi loi dat ten

# 1diem: Sai - Bat dau bang chu so (sua: diem1)
# gia-tri: Sai - Chua dau gach ngang (sua: gia_tri)
# _tam_thoi: Dung - Bat dau bang dau _ hop le
# Diem_TB: Dung - Dat ten kieu Snake_case hop le
# class: Sai - Trung tu khoa keyword cua Python
# so luong: Sai - Chua khoang trang
# MAX_SPEED: Dung - Viet hoa hang so hop le
# diemTB: Dung - Dat ten kieu camelCase hop le
# 2024_data: Sai - Bat dau bang chu so (sua: data_2024)
# tong$: Sai - Chua ky tu dac biet $
# sinhVien1: Dung - Chu so dung o cuoi hop le

# 3.2 - Áp dụng PEP8

Ten = "Nguyen Van A"
DiemToan = 8.5
DiemVan = 7.0
SoLuongMonHoc = 2
MUCLUONGTOITHIEU = 5000000  # đây là một hằng số

print("Họ và tên:", Ten)
print("Điểm toán:", DiemToan)
print("Điểm văn:", DiemVan)
print("Số lượng môn học:", SoLuongMonHoc)
print("Mức lương tối thiểu:", MUCLUONGTOITHIEU)

# 5.1 - Toán tử số học

a = 17
b = 5

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)


# 5.2 - Toán tử so sánh và logic

diem = 6.5
tuoi = 26

diem_kha = diem >= 6.5 and diem < 8.0
print("Điểm đạt loại khá:", diem_kha)

tuoi_khong_hop_le = tuoi < 18 or tuoi > 60
print("Tuổi không hợp lệ:", tuoi_khong_hop_le)

# 5.3 - Toán tử gán và toán tử đặc biệt
x = 10

x += 5
print("x sau += 5:", x)

x -= 3
print("x sau -= 3:", x)

x *= 2
print("x sau *= 2:", x)

x /= 2
print("x sau /= 2:", x)

x //= 2
print("x sau //= 2:", x)

x **= 3
print("x sau **= 3:", x)

danh_sach = [1, 2, 3, "python"]
print("3 có trong danh_sach không?:", 3 in danh_sach)

list_a = [1, 2, 3]
list_b = list_a
list_c = [1, 2, 3]

print("list_a is list_b:", list_a is list_b)
print("list_a is list_c:", list_a is list_c)

# 5.4 - Độ ưu tiên toán tử

ket_qua_1 = 2 + 3 * 4 ** 2
print("Kết quả 1:", ket_qua_1)

ket_qua_2 = (2 + 3) * 4 ** 2
print("Kết quả 2:", ket_qua_2)

ket_qua_3 = 10 > 5 and 3 < 1 or not False
print("Kết quả 3:", ket_qua_3)


# 6.1 - Kiểu dữ liệu của biến

bien = 10
print(bien, type(bien))

bien = "Xin chao"
print(bien, type(bien))

bien = 3.14
print(bien, type(bien))

bien = True
print(bien, type(bien))

# 6.2 - Tính điểm trung bình và xếp loại

ho_ten = "Do Dong Minh"
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
print("Kiểu dữ liệu của loại giỏi:", type(loai_gioi))