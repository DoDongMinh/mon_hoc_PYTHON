
import tkinter as tk
from tkinter import ttk

cua_so = tk.Tk()
cua_so.title("Vi du Listbox va Combobox")
cua_so.geometry("380x420")

# BÀI TẬP 3.1: LISTBOX
tk.Label(
    cua_so,
    text="Chon mon hoc (Listbox):",
    font=("Arial", 11, "bold")
).pack(pady=(10, 5))

listbox_mon_hoc = tk.Listbox(
    cua_so,
    selectmode="single",
    height=5
)

for mon in ["Toan", "Ly", "Hoa", "Van", "Anh"]:
    listbox_mon_hoc.insert(tk.END, mon)

listbox_mon_hoc.pack(pady=5)
nhan_ket_qua_listbox = tk.Label(cua_so, text="")
nhan_ket_qua_listbox.pack(pady=3)

def xem_mon_da_chon():
    lua_chon = listbox_mon_hoc.curselection()

    if lua_chon:
        mon = listbox_mon_hoc.get(lua_chon[0])
        nhan_ket_qua_listbox.config(
            text=f"Mon da chon: {mon}"
        )
    else:
        nhan_ket_qua_listbox.config(
            text="Ban chua chon mon hoc."
        )


tk.Button(
    cua_so,
    text="Xem mon da chon",
    command=xem_mon_da_chon
).pack(pady=3)

# BÀI TẬP 3.2: COMBOBOX=
tk.Label(
    cua_so,
    text="Chon thanh pho (Combobox):",
    font=("Arial", 11, "bold")
).pack(pady=(15, 5))

combobox_thanh_pho = ttk.Combobox(
    cua_so,
    values=["Ha Noi", "Da Nang", "TP.HCM", "Hue"],
    state="readonly"
)

combobox_thanh_pho.current(0)
combobox_thanh_pho.pack(pady=5)
nhan_ket_qua_combobox = tk.Label(cua_so, text="")
nhan_ket_qua_combobox.pack(pady=3)

def xem_thanh_pho():
    thanh_pho = combobox_thanh_pho.get()
    nhan_ket_qua_combobox.config(
        text=f"Ban chon: {thanh_pho}"
    )

tk.Button(
    cua_so,
    text="Xac nhan thanh pho",
    command=xem_thanh_pho
).pack(pady=5)

cua_so.mainloop()
