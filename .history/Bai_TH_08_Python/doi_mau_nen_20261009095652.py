# Bài tập 4.1
'''
import tkinter as tk 
danh_sach_mau = ["white", "lightblue", "lightgreen", "lightyellow", "lightpink"] 
vi_tri_mau_hien_tai = 0 
def doi_mau_nen():



 global vi_tri_mau_hien_tai 
 vi_tri_mau_hien_tai = (vi_tri_mau_hien_tai + 1) % len(danh_sach_mau)  
 cua_so.configure(bg=danh_sach_mau[vi_tri_mau_hien_tai]) 
cua_so = tk.Tk() 
cua_so.title("Doi mau nen") 
cua_so.geometry("350x200") 
nut_doi_mau = tk.Button(cua_so, text="Doi mau nen", command=doi_mau_nen) 
nut_doi_mau.pack(pady=80) 
cua_so.mainloop()

'''
# Bài tập 4.2 
'''
import tkinter as tk 
so_lan_bam = 0 
def tang_so_lan_bam(): 
 global so_lan_bam 
 so_lan_bam += 1 
 nhan_dem.config(text=f"So lan da bam: {so_lan_bam}") 
cua_so = tk.Tk() 
cua_so.title("Dem so lan bam nut") 
cua_so.geometry("350x200") 
nhan_dem = tk.Label(cua_so, text="So lan da bam: 0", font=("Arial", 14)) 
nhan_dem.pack(pady=20) 
nut_bam = tk.Button(cua_so, text="Bam vao day", command=tang_so_lan_bam) 
nut_bam.pack(pady=10) 
cua_so.mainloop()

'''

# Bài tâp 4.3 
import tkinter as tk 
def khi_go_phim(event): 
 nhan_thong_bao.config(text=f"Ban vua nhan phim: {event.char}") 
def khi_click_chuot(event): 
 nhan_thong_bao.config(text=f"Ban vua click tai toa do: ({event.x}, {event.y})") 
cua_so = tk.Tk() 
cua_so.title("Vi du bind()")



cua_so.geometry("400x250") 
nhan_thong_bao = tk.Label(cua_so, text="Hay go phim hoac click chuot", font=("Arial",  12)) 
nhan_thong_bao.pack(pady=30) 
cua_so.bind("<Key>", khi_go_phim) 
cua_so.bind("<Button-1>", khi_click_chuot) 
cua_so.mainloop()

#giải thích khác nhau giữa cách gắn sự kiện qua tham số command (chỉ dùng cho widget như  Button) và qua bind() 
# (dùng được cho nhiều loại sự kiện và nhiều widget, kể cả cửa sổ chính). 
'''
command:
 - Chỉ áp dụng cho một số widget hỗ trợ hành động kích hoạt trực tiếp (như Button).
 - Chỉ bắt được sự kiện "nhấp chuột/kích hoạt" mặc định, hàm xử lý không nhận tham số đối tượng sự kiện (event).

bind():

 - Dùng được cho tất cả các widget và cả cửa sổ chính (Tk).
 - Bắt được đa dạng các sự kiện phần cứng/hệ thống: gõ phím (<Key>), di chuyển chuột (<Motion>), cuộn chuột, nhấp chuột trái/phải 
   (<Button-1>, <Button-3>), thay đổi kích thước (<Configure>).
 - Hàm xử lý bắt buộc phải nhận tham số event chứa thông tin chi tiết (tọa độ chuột, phím được nhấn,...).
'''


