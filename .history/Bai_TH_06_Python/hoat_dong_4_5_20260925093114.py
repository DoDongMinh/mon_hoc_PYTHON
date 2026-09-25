# HOẠT ĐỘNG 4: Phạm vi biến - local, global, từ khóa global
so_luot_truy_cap = 0 # bien global

def tang_luot_truy_cap():
    global so_luot_truy_cap
    so_luot_truy_cap += 1

def vi_du_bien_local():
    so_luot_truy_cap = 100 # day la bien LOCAL, khac voi bien global cung ten
    print("Ben trong ham, bien local =", so_luot_truy_cap)

tang_luot_truy_cap()
tang_luot_truy_cap()
print("So luot truy cap (global):", so_luot_truy_cap)

vi_du_bien_local()
print("Sau khi goi ham, bien global van la:", so_luot_truy_cap)
# ❓ Yêu cầu: Giải thích vì sao nếu bỏ dòng global so_luot_truy_cap trong hàm tang_luot_truy_cap(), chương trình sẽ báo lỗi UnboundLocalError.
'''
  - Trong Python, khi một biến được gán giá trị (ở đây là biểu thức so_luot_truy_cap += 1 tương đương so_luot_truy_cap = so_luot_truy_cap + 1) bên trong một hàm,
    Python sẽ tự động coi biến đó là biến cục bộ (local variable).   
  - Nếu không khai báo global so_luot_truy_cap, ở vế phải của phép gán (so_luot_truy_cap + 1), Python sẽ cố tìm giá trị của biến cục bộ so_luot_truy_cap trước khi nó kịp 
    được gán giá trị. Việc đọc một biến cục bộ chưa khởi tạo dẫn đến lỗi UnboundLocalError: local variable 'so_luot_truy_cap' referenced before assignment.   
'''

# HOẠT ĐỘNG 5: Hàm lambda kết hợp map(), filter(), sorted()
# Bài tập 5.1 - map() với lambda
danh_sach_so = [1, 2, 3, 4, 5]
binh_phuong = list(map(lambda x: x ** 2, danh_sach_so))
print(binh_phuong)

# Bài tập 5.2 - filter() với lambda
so_chan = list(filter(lambda x: x % 2 == 0, danh_sach_so))
print(so_chan)

# Bài tập 5.3 - sorted() với lambda: sắp xếp danh sách sinh viên theo điểm
danh_sach_sv = [
    {"ten": "An", "diem": 8.5},
    {"ten": "Binh", "diem": 7.0},
    {"ten": "Chi", "diem": 9.2},
]

sap_xep_theo_diem = sorted(danh_sach_sv, key=lambda sv: sv["diem"])
sap_xep_giam_dan = sorted(danh_sach_sv, key=lambda sv: sv["diem"], reverse=True)

for sv in sap_xep_theo_diem:
    print(sv["ten"], "-", sv["diem"])

print("--- Giam dan ---")
for sv in sap_xep_giam_dan:
    print(sv["ten"], "-", sv["diem"])

# Yêu cầu: So sánh cách sắp xếp này với cách "đặt điểm trước tên trong tuple" đã dùng ở Buổi 3 — vì sao dùng key=lambda linh hoạt hơn?
'''
   Đặt điểm trước tên trong tuple ((diem, ten)): Yêu cầu phải biến đổi cấu trúc dữ liệu ban đầu hoặc tạo danh sách tạm. Khi so sánh tuple, 
   Python sẽ luôn so sánh phần tử thứ nhất trước (diem), nếu bằng nhau mới so sánh phần tử thứ hai (ten), làm bó hẹp tiêu chí và khó đáp ứng
   các điều kiện sắp xếp phức tạp.Sử dụng key=lambda linh hoạt hơn vì:
      - Giữ nguyên cấu trúc dữ liệu: Không cần thay đổi kiểu dữ liệu gốc (vẫn giữ nguyên dict hoặc object).   
      - Tùy biến đa dạng tiêu chí: Dễ dàng thay đổi khóa sắp xếp (theo tên, theo điểm, theo nhiều tiêu chuẩn kết hợp) chỉ bằng cách đổi 
        hàm lambda trả về.   
      - Tối ưu bộ nhớ & hiệu năng: Không tạo thêm dữ liệu trung gian thừa.   
'''
