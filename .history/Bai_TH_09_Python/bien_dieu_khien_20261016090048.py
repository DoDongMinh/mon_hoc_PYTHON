# Hoạt động 5
import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Vi du bien dieu khien")
cua_so.geometry("390x250")

bien_ho_ten = tk.StringVar(value="Nguyen Van A")

bien_tuoi = tk.IntVar(value=18)

bien_dong_y_dieu_khoan = tk.BooleanVar(value=False)

tk.Label(cua_so, text="Ho ten:").grid(
    row=0, column=0, padx=10, pady=10, sticky="w"
)

tk.Entry(
    cua_so,
    textvariable=bien_ho_ten,
    width=25
).grid(row=0, column=1, padx=10, pady=10)

tk.Label(cua_so, text="Tuoi:").grid(
    row=1, column=0, padx=10, pady=10, sticky="w"
)

tk.Entry(
    cua_so,
    textvariable=bien_tuoi,
    width=25
).grid(row=1, column=1, padx=10, pady=10)

tk.Checkbutton(
    cua_so,
    text="Dong y dieu khoan",
    variable=bien_dong_y_dieu_khoan
).grid(row=2, column=0, columnspan=2, pady=10)

def xem_gia_tri_bien():
    # get() đọc giá trị hiện tại trong các biến.
    print("Ho ten:", bien_ho_ten.get())
    print("Tuoi:", bien_tuoi.get())
    print(
        "Dong y dieu khoan:",
        bien_dong_y_dieu_khoan.get()
    )
    bien_tuoi.set(bien_tuoi.get() + 1)

tk.Button(
    cua_so,
    text="Xem gia tri bien (va +1 tuoi)",
    command=xem_gia_tri_bien
).grid(row=3, column=0, columnspan=2, pady=10)

cua_so.mainloop()

# Trả lời:  Giải thích vì sao dùng textvariable=bien_ho_ten thay vì phải gọi entry.get() mỗi lần cần lấy  giá trị - biến
# điều khiển mang lại lợi ích gì khi có nhiều widget cùng cần đọc/ghi một giá trị? 
'''
Sử dụng textvariable giúp liên kết trực tiếp ô nhập với biến điều khiển. Khi nội dung ô nhập thay đổi, giá trị trong biến cũng được cập nhật. Ngược 
lại, khi gọi set() để thay đổi biến, giao diện sẽ cập nhật theo.
Lợi ích:
  - Đồng bộ dữ liệu: biến và widget được liên kết tự động đồng bộ.
  - Dễ quản lý: có thể lấy dữ liệu bằng get() và thay đổi bằng set().
  - Chia sẻ dữ liệu: nhiều widget có thể cùng liên kết với một biến điều khiển.
  - Giảm thao tác thủ công: không cần liên tục lấy dữ liệu từ từng ô nhập để cập nhật giao diện.
'''
