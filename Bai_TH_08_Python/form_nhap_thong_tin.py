import tkinter as tk

def xu_ly_submit():
    ho_ten = entry_ho_ten.get()
    tuoi = entry_tuoi.get()
    email = entry_email.get()
    nhan_ket_qua.config(
        text=f"Da nhan: {ho_ten} - {tuoi} tuoi - {email}"
    )

def xu_ly_xoa():
    # Xóa toàn bộ ký tự từ vị trí 0 đến END trong các ô nhập
    entry_ho_ten.delete(0, tk.END)
    entry_tuoi.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    nhan_ket_qua.config(text="")

cua_so = tk.Tk()
cua_so.title("Form nhap thong tin")
cua_so.geometry("420x300")
cua_so.resizable(False, False)

tk.Label(cua_so, text="Ho ten:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_ho_ten = tk.Entry(cua_so, width=28)
entry_ho_ten.grid(row=0, column=1, padx=10, pady=10)
tk.Label(cua_so, text="Tuoi:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_tuoi = tk.Entry(cua_so, width=28)
entry_tuoi.grid(row=1, column=1, padx=10, pady=10)
tk.Label(cua_so, text="Email:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_email = tk.Entry(cua_so, width=28)
entry_email.grid(row=2, column=1, padx=10, pady=10)

# Khung chứa nút bấm (Submit & Xóa) 
khung_nut = tk.Frame(cua_so)
khung_nut.grid(row=3, column=0, columnspan=2, pady=10)
nut_submit = tk.Button(khung_nut, text="Submit", width=10, command=xu_ly_submit)
nut_submit.pack(side="left", padx=10)
nut_xoa = tk.Button(khung_nut, text="Xoa", width=10, command=xu_ly_xoa)
nut_xoa.pack(side="left", padx=10)
nhan_ket_qua = tk.Label(cua_so, text="", font=("Arial", 11), fg="blue")
nhan_ket_qua.grid(row=4, column=0, columnspan=2, pady=10)
cua_so.mainloop()