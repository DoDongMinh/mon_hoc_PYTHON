# Bài tập bổ sung
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("May tinh bo tui")
root.geometry("340x460")
root.resizable(False, False)
bieu_thuc = ""
ket_qua = tk.StringVar(value="0")

man_hinh = tk.Entry(
    root,
    textvariable=ket_qua,
    font=("Arial", 24),
    justify="right",
    state="readonly",
    readonlybackground="white",
    bd=5
)
man_hinh.grid(row=0, column=0, columnspan=4,
              padx=10, pady=20, ipady=15, sticky="nsew")

def them_ky_tu(ky_tu):
    global bieu_thuc

    if ket_qua.get() == "Loi":
        bieu_thuc = ""

    bieu_thuc += ky_tu
    ket_qua.set(bieu_thuc)

def xoa_tat_ca():
    global bieu_thuc
    bieu_thuc = ""
    ket_qua.set("0")

def xoa_mot_ky_tu():
    global bieu_thuc
    bieu_thuc = bieu_thuc[:-1]
    ket_qua.set(bieu_thuc if bieu_thuc else "0")

def tinh_ket_qua():
    global bieu_thuc

    try:
        phep_toan_hop_le = set("0123456789.+-*/() ")

        if not bieu_thuc or any(
            ky_tu not in phep_toan_hop_le for ky_tu in bieu_thuc
        ):
            raise ValueError

        ket_qua_tinh = eval(
            bieu_thuc,
            {"__builtins__": {}},
            {}
        )

        if isinstance(ket_qua_tinh, (int, float)):
            if isinstance(ket_qua_tinh, float) and ket_qua_tinh.is_integer():
                ket_qua_tinh = int(ket_qua_tinh)

            ket_qua.set(str(ket_qua_tinh))
            bieu_thuc = str(ket_qua_tinh)

    except ZeroDivisionError:
        ket_qua.set("Loi: chia cho 0")
        bieu_thuc = ""
    except (ValueError, SyntaxError, TypeError, OverflowError):
        ket_qua.set("Loi")
        bieu_thuc = ""

cac_nut = [
    ("C", xoa_tat_ca, 1, 0),
    ("DEL", xoa_mot_ky_tu, 1, 1),
    ("(", lambda: them_ky_tu("("), 1, 2),
    (")", lambda: them_ky_tu(")"), 1, 3),

    ("7", lambda: them_ky_tu("7"), 2, 0),
    ("8", lambda: them_ky_tu("8"), 2, 1),
    ("9", lambda: them_ky_tu("9"), 2, 2),
    ("/", lambda: them_ky_tu("/"), 2, 3),

    ("4", lambda: them_ky_tu("4"), 3, 0),
    ("5", lambda: them_ky_tu("5"), 3, 1),
    ("6", lambda: them_ky_tu("6"), 3, 2),
    ("*", lambda: them_ky_tu("*"), 3, 3),

    ("1", lambda: them_ky_tu("1"), 4, 0),
    ("2", lambda: them_ky_tu("2"), 4, 1),
    ("3", lambda: them_ky_tu("3"), 4, 2),
    ("-", lambda: them_ky_tu("-"), 4, 3),

    ("0", lambda: them_ky_tu("0"), 5, 0),
    (".", lambda: them_ky_tu("."), 5, 1),
    ("=", tinh_ket_qua, 5, 2),
    ("+", lambda: them_ky_tu("+"), 5, 3)
]

# Tao va sap xep cac nut tren giao dien
for ten, hanh_dong, hang, cot in cac_nut:
    nut = tk.Button(
        root,
        text=ten,
        font=("Arial", 16),
        command=hanh_dong,
        width=5,
        height=2
    )
    nut.grid(
        row=hang,
        column=cot,
        padx=4,
        pady=4,
        sticky="nsew"
    )

for cot in range(4):
    root.grid_columnconfigure(cot, weight=1)

root.mainloop()
