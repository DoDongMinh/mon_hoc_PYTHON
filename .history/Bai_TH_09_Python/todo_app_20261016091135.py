
import tkinter as tk
from tkinter import messagebox

danh_sach_cong_viec = []

def lam_moi_listbox():
    listbox_cong_viec.delete(0, tk.END)

    for noi_dung, da_hoan_thanh in danh_sach_cong_viec:
        if da_hoan_thanh:
            tien_to = "[Da xong] "
        else:
            tien_to = "[Chua xong] "

        listbox_cong_viec.insert(
            tk.END,
            tien_to + noi_dung
        )

def them_cong_viec():
    noi_dung = bien_cong_viec_moi.get().strip()

    if noi_dung == "":
        messagebox.showerror(
            "Loi",
            "Vui long nhap noi dung cong viec truoc khi them."
        )
        return
    danh_sach_cong_viec.append((noi_dung, False))
    bien_cong_viec_moi.set("")

    lam_moi_listbox()

def xoa_cong_viec():
    lua_chon = listbox_cong_viec.curselection()
    if not lua_chon:
        messagebox.showerror(
            "Loi",
            "Vui long chon mot cong viec trong danh sach de xoa."
        )
        return
    vi_tri = lua_chon[0]
    danh_sach_cong_viec.pop(vi_tri)
    lam_moi_listbox()

def danh_dau_hoan_thanh():
    lua_chon = listbox_cong_viec.curselection()
    if not lua_chon:
        messagebox.showerror(
            "Loi",
            "Vui long chon mot cong viec de danh dau hoan thanh."
        )
        return

    vi_tri = lua_chon[0]
    noi_dung, da_hoan_thanh = danh_sach_cong_viec[vi_tri]

    if da_hoan_thanh:
        messagebox.showinfo(
            "Thong bao",
            "Cong viec nay da duoc danh dau hoan thanh."
        )
        return
    danh_sach_cong_viec[vi_tri] = (noi_dung, True)
    lam_moi_listbox()

# THIẾT KẾ GIAO DIỆN
cua_so = tk.Tk()
cua_so.title("Ung dung Ghi chu cong viec")
cua_so.geometry("520x430")
cua_so.resizable(False, False)
bien_cong_viec_moi = tk.StringVar()

tk.Label(
    cua_so,
    text="TO-DO LIST",
    font=("Arial", 16, "bold")
).grid(row=0, column=0, columnspan=3, pady=15)
entry_cong_viec = tk.Entry(
    cua_so,
    textvariable=bien_cong_viec_moi,
    width=35
)
entry_cong_viec.grid(
    row=1, column=0, columnspan=2, padx=10, pady=5
)
entry_cong_viec.focus()

tk.Button(
    cua_so,
    text="Them",
    width=10,
    command=them_cong_viec
).grid(row=1, column=2, padx=10, pady=5)
listbox_cong_viec = tk.Listbox(
    cua_so,
    width=55,
    height=14,
    selectmode="single"
)
listbox_cong_viec.grid(
    row=2, column=0, columnspan=3, padx=10, pady=10
)

tk.Button(
    cua_so,
    text="Danh dau hoan thanh",
    command=danh_dau_hoan_thanh
).grid(row=3, column=0, padx=8, pady=10)

tk.Button(
    cua_so,
    text="Xoa cong viec",
    command=xoa_cong_viec
).grid(row=3, column=1, padx=8, pady=10)

tk.Button(
    cua_so,
    text="Thoat",
    command=cua_so.destroy
).grid(row=3, column=2, padx=8, pady=10)
entry_cong_viec.bind(
    "<Return>",
    lambda event: them_cong_viec()
)
if __name__ == "__main__":
    cua_so.mainloop()
