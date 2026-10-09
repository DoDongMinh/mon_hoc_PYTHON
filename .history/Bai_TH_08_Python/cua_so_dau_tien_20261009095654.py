'''
import tkinter as tk 
cua_so = tk.Tk() 
cua_so.title("Ung dung demo") 
cua_so.geometry("400x300") 
cua_so.resizable(False, False) # khong cho keo rong/cao 
nhan = tk.Label(cua_so, text="Xin chao Tkinter!", font=("Arial", 16)) 
nhan.pack(pady=20) 
cua_so.mainloop()
# Yêu cầu: thử đổi resizable(False, False) thành resizable(True, False), quan sát sự khác biệt khi kéo cửa  sổ. 
    -Khi đổi thành resizable(True, False): Cửa sổ cho phép kéo giãn theo chiều rộng 
    (chiều ngang - width=True), nhưng cố định chiều cao (chiều dọc - height=False).
'''
import tkinter as tk 
cua_so = tk.Tk() 
cua_so.title("Vi du Frame") 
cua_so.geometry("400x300") 
khung_tren = tk.Frame(cua_so, bg="lightblue", height=100) 
khung_tren.pack(fill="x") 
khung_duoi = tk.Frame(cua_so, bg="lightyellow") 
khung_duoi.pack(fill="both", expand=True) 
tk.Label(khung_tren, text="Khu vuc tieu de", bg="lightblue").pack(pady=10) 
tk.Label(khung_duoi, text="Khu vuc noi dung", bg="lightyellow").pack(pady=10) 
cua_so.mainloop()

#Yêu cầu: giải thích vai trò của Frame - vì sao nên nhóm các widget liên quan vào cùng một Frame thay vì  đặt hết trực tiếp lên cửa sổ chính. 
'''
Vai trog vủa Frame:
 - Gom nhóm & Quản lý: Frame đóng vai trò như một "hộp chứa" giúp nhóm các widget có liên quan 
   lại với nhau (ví dụ: thanh tiêu đề, menu điều hướng, nội dung chính, thanh công cụ).

 - Bố cục linh hoạt: Cho phép kết hợp các loại trình quản lý bố cục khác nhau (pack, grid) trên cùng
   một cửa sổ chính. Ví dụ: Cửa sổ chính dùng pack() để xếp các Frame trên/dưới, còn bên trong mỗi Frame 
   lại dùng grid() để xếp nút/ô nhập liệu.

 - Bảo trì dễ dàng: Giúp mã nguồn rõ ràng, dễ chỉnh sửa hoặc di chuyển nguyên khối giao diện mà không 
   ảnh hưởng đến các phần khác.
'''
