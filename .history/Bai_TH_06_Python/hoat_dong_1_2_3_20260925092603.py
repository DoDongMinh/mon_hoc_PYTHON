# HOẠT ĐỘNG 1: Hàm cơ bản - def, tham số, return
# Bài tập 1.1 - Viết hàm và gọi lại nhiều lần
def uscln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def bscnn(a, b):
    return a * b // uscln(a, b)

def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def kiem_tra_so_hoan_thien(n):
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n

print(uscln(24, 36))
print(bscnn(4, 6))
print(kiem_tra_nguyen_to(29))
print(kiem_tra_so_hoan_thien(28))

# Bài tập 1.2 - return không giá trị và trả về nhiều giá trị
def in_loi_chao(ten):
    print(f"Xin chao, {ten}!")
    return # ham khong tra ve gia tri (tra ve None)

def chia_lay_thuong_du(a, b):
    return a // b, a % b # tra ve nhieu gia tri qua tuple

in_loi_chao("An")
thuong, du = chia_lay_thuong_du(17, 5)
print(f"Thuong: {thuong}, du: {du}")

# HOẠT ĐỘNG 2: Tham số mặc định & tham số từ khóa
def gioi_thieu(ten, tuoi=18, lop="Chua ro"):
    print(f"Ten: {ten} - Tuoi: {tuoi} - Lop: {lop}")

gioi_thieu("An")                           # dung het gia tri mac dinh
gioi_thieu("Binh", 20)                     # ghi de tuoi
gioi_thieu("Chi", lop="CNTT01")            # dung tham so tu khoa, bo qua tuoi
gioi_thieu(ten="Dung", lop="CNTT02", tuoi=19) # thu tu tham so tu khoa co the dao lon
# Yêu cầu: Giải thích vì sao khi gọi hàm bằng tham số từ khóa (ten=..., lop=...) thì thứ tự truyền vào không quan trọng.
'''
  Khi truyền theo kiểu tham số vị trí, python gán giá trị cho tham số dựa vào thứ tự xuất hiện. Ngược lại, 
  khi dùng tham số từ khóa:   
    - Python xác định tham số dựa trên tên (key/identifier) trực tiếp đã gắn với tham số đó chứ không dựa vào thứ tự hiển thị.   
    - Trình biên dịch của Python tra cứu tên tham số được truyền trong chữ ký hàm (function signature) để khớp dữ liệu trực tiếp, 
      giúp việc thay đổi thứ tự các từ khóa không làm ảnh hưởng tới kết quả truyền.   
'''

# Hoạt động 3: Tham số linh hoạt - *args và **kwargs
# Bài tập 3.1 - *args: tính tổng số lượng bất kỳ các số
def tinh_tong(*args):
    tong = 0
    for so in args:
        tong += so
    return tong

print(tinh_tong(1, 2, 3))
print(tinh_tong(5, 10, 15, 20, 25))
print(tinh_tong()) # khong truyen so nao -> tra ve 0

# Bài tập 3.2 - **kwargs: in thông tin động
def in_thong_tin(ho_ten, tuoi, **kwargs):
    print(f"Ho ten: {ho_ten} - Tuoi: {tuoi}")
    for khoa, gia_tri in kwargs.items():
        print(f"  {khoa}: {gia_tri}")

in_thong_tin("Nguyen Van A", 20, lop="CNTT01", que_quan="Ha Noi")
in_thong_tin("Tran Thi B", 21, email="b@example.com")