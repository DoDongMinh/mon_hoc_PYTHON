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

#hoat dong 3.2: ap dung PEP8
ten = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2
MUC_LUONG_TOI_THIEU = 5000000 # đây là một hằng số

print(ten, diem_toan, diem_van, so_luong_mon_hoc, MUC_LUONG_TOI_THIEU)

#hoat dong 5.1: toan tu so hoc

a = 17
b = 5

tong = a + b
hieu = a - b
tich = a * b
thuong = a / b
chia_lay_nguyen = a // b
chia_lay_du = a % b
luy_thua = a ** b

print(tong, hieu, tich, thuong, chia_lay_nguyen, chia_lay_du, luy_thua)

#hoat dong 5.2: toan tu so sanh va logic
diem = 6.5
tuoi = 20

logic_and = (diem >= 6.5) and (diem < 8)
logic_or = (tuoi < 18) or (tuoi > 60)
logic_not_and = not logic_and
logic_not_or = not logic_or

print(logic_and, logic_or, logic_not_and, logic_not_or)

#hoat dong 5.3: toan tu gan va toan tu dac biet
x = 10
x += 5 # tương đương x = x + 5
print(x)
x -= 5
print(x)
x *= 5
print(x)
x /= 5
print(x)
x //= 5
print(x)
x **= 5
print(x)
# Yêu cầu: viết tiếp với -=, *=, /=, //=, **= và in giá trị x sau mỗi bước

danh_sach = [1, 2, 3, "python"]
# Dùng toán tử "in" để kiểm tra 3 có trong danh_sach không
toan_tu_in = 3 in danh_sach
# Dùng toán tử "is" để so sánh 2 biến cùng tham chiếu tới 1 list
danh_sach_goc = danh_sach
toan_tu_is = danh_sach_goc is danh_sach

print(toan_tu_in, toan_tu_is)

#hoat dong 5.4: do uu tien toan tu

print(2 + 3 * 4 ** 2)
#kq: 50
print((2 + 3) * 4 ** 2)
#kq: 80
print(10 > 5 and 3 < 1 or not False)
#kq: true

#hoat dong 6.1: khai bao lan luot cac bien voi kieu du lieu khac nhau va in bang kieu type
bien = 10
print(bien, type(bien))
bien = "Xin chao"
print(bien, type(bien))
bien = 3.14
print(bien, type(bien))
bien = True
print(bien, type(bien))
# Cau hoi: Vi sao cung mot bien bien co the mang nhieu kieu du lieu khac nhau trong Python? Dieu nay khac gi so voi khai bao bien trong C/C++/Java ma cac ban da hoc (vi du int bien = 10;)?
# tra loi: vì biến trong python là kiểu động, khi khai báo biến kèm dữ liệu biến sẽ tự xác định ra kiểu dữ liệu mà không cần khai báo kiểu như java hay c++

#hoat dong 6.2 mini bai toan tong hop

ho_ten = "Nguyen Trong Tien"

diem_toan = 9
diem_ly = 10
diem_hoa = 8

diem_trung_binh = (diem_toan + diem_ly + diem_hoa) / 3

loai_gioi = diem_trung_binh >= 8.0
loai_kha = diem_trung_binh >= 6.5 and diem_trung_binh < 8.0
loai_trung_binh = diem_trung_binh >= 5.0 and diem_trung_binh < 6.5
loai_yeu = diem_trung_binh < 5.0

print ("ho va ten:", ho_ten)
print ("diem trung binh:", diem_trung_binh)
print ("xep loai gioi:", loai_gioi)
print ("xep loai kha:", loai_kha)
print ("xep loai trung binh:", loai_trung_binh)
print ("xep loai yeu:", loai_yeu)
print ("kieu du lieu cua loai_gioi:", type(loai_gioi))