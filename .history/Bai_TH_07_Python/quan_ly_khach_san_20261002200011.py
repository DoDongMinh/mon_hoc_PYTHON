# Đồ án nhỏ Buổi 7: Quản lý đặt phòng khách sạn mini trên Console
# 1. KHAI BÁO DỮ LIỆU BÂN ĐẦU
danh_sach_phong = [
    {"ma_phong": "P101", "loai_phong": "Don", "gia": 300000, "trang_thai": "Trong", "ten_khach": ""},
    {"ma_phong": "P102", "loai_phong": "Doi", "gia": 500000, "trang_thai": "Trong", "ten_khach": ""},
    {"ma_phong": "P103", "loai_phong": "VIP", "gia": 900000, "trang_thai": "Trong", "ten_khach": ""},
    {"ma_phong": "P104", "loai_phong": "Don", "gia": 300000, "trang_thai": "Trong", "ten_khach": ""},
]

lich_su_doanh_thu = []

# 2. HÀM HỖ TRỢ & BẮT LỖI (Ttry-except)

def nhap_so_nguyen_duong(loi_nhac):
    """
    Hàm bắt lỗi nhập số nguyên bằng try-except.
    Đảm bảo người dùng phải nhập số nguyên lớn hơn 0, không làm crash chương trình.
    """
    while True:
        try:
            val = int(input(loi_nhac))
            if val > 0:
                return val
            print("-> Lỗi: Giá trị phải là số nguyên lớn hơn 0, vui lòng nhập lại.")
        except ValueError:
            print("-> Lỗi: Định dạng không hợp lệ! Vui lòng nhập một số nguyên.")


def tim_phong_theo_ma(ma_phong):
    """Hàm tìm kiếm phòng trong danh sách theo mã phòng (không phân biệt hoa/thường)."""
    for phong in danh_sach_phong:
        if phong["ma_phong"].upper() == ma_phong.upper():
            return phong
    return None

# 3. CÁC HÀM CHỨC NĂNG NGHIỆP VỤ (CRUD)

def hien_thi_danh_sach_phong():
    """Chức năng 1: Hiển thị bảng toàn bộ danh sách phòng."""
    print("\n" + "=" * 70)
    print(f"{'Mã phòng':<10}{'Loại phòng':<12}{'Giá/đêm (VND)':<18}{'Trạng thái':<15}{'Tên khách':<15}")
    print("-" * 70)
    for phong in danh_sach_phong:
        khach = phong["ten_khach"] if phong["ten_khach"] else "-"
        print(f"{phong['ma_phong']:<10}{phong['loai_phong']:<12}{phong['gia']:<18,}{phong['trang_thai']:<15}{khach:<15}")
    print("=" * 70)


def xem_phong_trong():
    """Chức năng 2: Lọc và hiển thị các phòng đang có trạng thái 'Trong'."""
    phong_trong = [p for p in danh_sach_phong if p["trang_thai"] == "Trong"]
    if not phong_trong:
        print("\n-> Hiện tại khách sạn không còn phòng trống nào.")
        return

    print("\n" + "-" * 50)
    print("DANH SÁCH PHÒNG ĐANG TRỐNG")
    print("-" * 50)
    for p in phong_trong:
        print(f" • Mã phòng: {p['ma_phong']:<6} | Loại: {p['loai_phong']:<8} | Giá: {p['gia']:,} VND/đêm")
    print("-" * 50)


def them_phong():
    """Chức năng 3: Thêm phòng mới vào danh sách."""
    print("\n--- THÊM PHÒNG MỚI ---")
    ma_phong = input("Nhập mã phòng mới (ví dụ: P105): ").strip().upper()
    if not ma_phong:
        print("-> Lỗi: Mã phòng không được để trống.")
        return

    if tim_phong_theo_ma(ma_phong) is not None:
        print(f"-> Lỗi: Mã phòng {ma_phong} đã tồn tại trong hệ thống.")
        return

    loai_phong = input("Nhập loại phòng (Don/Doi/VIP): ").strip().title()
    if not loai_phong:
        loai_phong = "Don"

    gia = nhap_so_nguyen_duong("Nhập giá phòng/đêm (VND): ")

    danh_sach_phong.append({
        "ma_phong": ma_phong,
        "loai_phong": loai_phong,
        "gia": gia,
        "trang_thai": "Trong",
        "ten_khach": ""
    })
    print(f"-> Đã thêm phòng {ma_phong} ({loai_phong}) thành công.")


def dat_phong():
    """Chức năng 4: Đặt phòng cho khách (Đổi trạng thái Trong -> Da dat)."""
    print("\n--- ĐẶT PHÒNG CHO KHÁCH ---")
    ma_phong = input("Nhập mã phòng cần đặt: ").strip().upper()
    phong = tim_phong_theo_ma(ma_phong)

    if phong is None:
        print(f"-> Lỗi: Không tìm thấy mã phòng {ma_phong}.")
        return

    if phong["trang_thai"] == "Da dat":
        print(f"-> Lỗi: Phòng {ma_phong} đã có khách ({phong['ten_khach']}), không thể đặt.")
        return

    ten_khach = input("Nhập tên khách hàng: ").strip().title()
    if not ten_khach:
        print("-> Lỗi: Tên khách hàng không được để trống.")
        return

    phong["trang_thai"] = "Da dat"
    phong["ten_khach"] = ten_khach
    print(f"-> Đặt phòng {ma_phong} cho khách '{ten_khach}' thành công!")


def tra_phong():
    """Chức năng 5: Trả phòng, tính tiền hóa đơn và ghi lịch sử giao dịch."""
    print("\n--- TRẢ PHÒNG & THANH TOÁN ---")
    ma_phong = input("Nhập mã phòng cần trả: ").strip().upper()
    phong = tim_phong_theo_ma(ma_phong)

    if phong is None:
        print(f"-> Lỗi: Không tìm thấy mã phòng {ma_phong}.")
        return

    if phong["trang_thai"] == "Trong":
        print(f"-> Lỗi: Phòng {ma_phong} đang trống, không có khách để trả.")
        return

    so_dem = nhap_so_nguyen_duong("Nhập số đêm khách đã ở: ")
    thanh_tien = phong["gia"] * so_dem

    # Lưu giao dịch vào lịch sử doanh thu
    lich_su_doanh_thu.append({
        "ma_phong": phong["ma_phong"],
        "ten_khach": phong["ten_khach"],
        "so_dem": so_dem,
        "thanh_tien": thanh_tien
    })

    # In hóa đơn
    print("\n" + "*" * 45)
    print("         HÓA ĐƠN THANH TOÁN")
    print(f" • Khách hàng : {phong['ten_khach']}")
    print(f" • Phòng      : {phong['ma_phong']} ({phong['loai_phong']})")
    print(f" • Đơn giá    : {phong['gia']:,} VND/đêm")
    print(f" • Số đêm ở   : {so_dem} đêm")
    print(f" >>> TỔNG TIỀN: {thanh_tien:,} VND")
    print("*" * 45)

    # Chuyển phòng về trạng thái Trống
    phong["trang_thai"] = "Trong"
    phong["ten_khach"] = ""
    print(f"-> Hoàn tất trả phòng {ma_phong}. Phòng đã sẵn sàng đón khách mới!")
    
def thong_ke_doanh_thu():
    """Chức năng 6: Báo cáo lịch sử trả phòng và tổng doanh thu."""
    print("\n" + "=" * 65)
    print("       THỐNG KÊ DOANH THU & LỊCH SỬ GIAO DỊCH")
    print("=" * 65)
    if not lich_su_doanh_thu:
        print("-> Chưa có giao dịch trả phòng nào được ghi nhận.")
        return
    tong_doanh_thu = 0
    print(f"{'Mã phòng':<10}{'Khách hàng':<20}{'Số đêm':<10}{'Thành tiền (VND)':<20}")
    print("-" * 65)
    for gd in lich_su_doanh_thu:
        print(f"{gd['ma_phong']:<10}{gd['ten_khach']:<20}{gd['so_dem']:<10}{gd['thanh_tien']:<20,}")
        tong_doanh_thu += gd["thanh_tien"]
    print("-" * 65)
    print(f" TỔNG DOANH THU TÍNH ĐẾN HIỆN TẠI : {tong_doanh_thu:,} VND")
    print(f" TỔNG SỐ LƯỢT TRẢ PHÒNG           : {len(lich_su_doanh_thu)} lượt")
    print("=" * 65)
# 4. ĐIỀU KHIỂN MENU CHÍNH

def hien_thi_menu():
    print("\n" + "★" * 12 + " QUẢN LÝ ĐẶT PHÒNG KHÁCH SẠN MINI " + "★" * 12)
    print(" 1. Hiển thị danh sách tất cả các phòng")
    print(" 2. Xem nhanh các phòng đang trống")
    print(" 3. Thêm phòng mới")
    print(" 4. Đặt phòng cho khách")
    print(" 5. Trả phòng / Thanh toán hóa đơn")
    print(" 6. Thống kê lịch sử giao dịch & Tổng doanh thu")
    print(" 0. Thoát chương trình")
    print("★" * 58)


def chay_chuong_trinh():
    while True:
        hien_thi_menu()
        lua_chon = input("Nhập lựa chọn của bạn (0-6): ").strip()

        if lua_chon == "1":
            hien_thi_danh_sach_phong()
        elif lua_chon == "2":
            xem_phong_trong()
        elif lua_chon == "3":
            them_phong()
        elif lua_chon == "4":
            dat_phong()
        elif lua_chon == "5":
            tra_phong()
        elif lua_chon == "6":
            thong_ke_doanh_thu()
        elif lua_chon == "0":
            print("\nCảm ơn bạn đã sử dụng phần mềm Quản lý Khách sạn Mini. Tạm biệt!")
            break
        else:
            print("-> Lỗi: Lựa chọn không hợp lệ! Vui lòng chọn số từ 0 đến 6.")


# Điểm khởi chạy chương trình
if __name__ == "__main__":
    chay_chuong_trinh()