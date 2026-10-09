#Bài tập 3.1
'''
import tkinter as tk 
cua_so = tk.Tk() 
cua_so.title("Bo cuc bang pack()") 
cua_so.geometry("300x250") 
tk.Label(cua_so, text="Ho ten:").pack(pady=5) 
tk.Label(cua_so, text="Tuoi:").pack(pady=5) 
tk.Label(cua_so, text="Email:").pack(pady=5) 
tk.Button(cua_so, text="Dong y").pack(side="left", padx=20, pady=15) 
tk.Button(cua_so, text="Huy").pack(side="right", padx=20, pady=15) 
cua_so.mainloop()
'''
#Bài tập 3.2
'''
import tkinter as tk 
cua_so = tk.Tk() 
cua_so.title("Bo cuc bang grid()") 
cua_so.geometry("300x250") 
tk.Label(cua_so, text="Ho ten:").grid(row=0, column=0, padx=10, pady=5, sticky="w") 
tk.Label(cua_so, text="Tuoi:").grid(row=1, column=0, padx=10, pady=5, sticky="w") 
tk.Label(cua_so, text="Email:").grid(row=2, column=0, padx=10, pady=5, sticky="w") 
tk.Button(cua_so, text="Dong y").grid(row=3, column=0, padx=10, pady=15) 
tk.Button(cua_so, text="Huy").grid(row=3, column=1, padx=10, pady=15) 
cua_so.mainloop()

'''
#Bài tập 3.3
import tkinter as tk 
cua_so = tk.Tk() 
cua_so.title("Bo cuc bang place()") 
cua_so.geometry("300x250") 
tk.Label(cua_so, text="Ho ten:").place(x=20, y=20) 
tk.Label(cua_so, text="Tuoi:").place(x=20, y=60) 
tk.Label(cua_so, text="Email:").place(x=20, y=100) 
tk.Button(cua_so, text="Dong y").place(x=40, y=160) 
tk.Button(cua_so, text="Huy").place(x=150, y=160) 
cua_so.mainloop()

#Câu hỏi:  pack() sắp xếp widget theo nguyên tắc nào (trên-dưới hay trái-phải)? Tham số side dùng để làm gì? • grid() phù hợp nhất với loại giao diện nào
# (gợi ý: form nhiều dòng nhãn + ô nhập)? • place() có ưu điểm và nhược điểm gì so với pack()/grid() khi cửa sổ bị thay đổi kích thước? 
'''
 - pack():Nguyên tắc: Sắp xếp các widget lần lượt dạt về các cạnh của khung chứa. Mặc định là dồn từ trên xuống dưới (side="top").Tham số 
   side: Dùng để định vị hướng dồn của widget. Các giá trị gồm: "top", "bottom", "left", "right".
 - grid():Phù hợp nhất với: Giao diện dạng bảng hoặc lưới gồm các dòng và cột (row, column), cực kỳ tối ưu cho Form nhập liệu (với nhãn bên 
   trái và ô nhập/nút bấm bên phải).
 - place():Ưu điểm: Cho phép đặt widget chính xác đến từng pixel theo tọa độ $(x, y)$.Nhược điểm: Mất tính co giãn tự động. Khi cửa sổ thay 
   đổi kích thước, các widget vẫn nằm cố định tại tọa độ cũ, dẫn đến việc bị che mất hoặc thừa khoảng trống không cân đối.
'''

