
import tkinter as tk

# HOẠT ĐỘNG 1: CHECKBUTTON
def mo_cua_so_checkbutton():
    cua_so = tk.Toplevel(root)
    cua_so.title("Vi du Checkbutton")
    cua_so.geometry("320x260")

    tk.Label(
        cua_so,
        text="Chon so thich cua ban:",
        font=("Arial", 12)
    ).pack(pady=10)

    # BooleanVar lưu trạng thái True/False của từng Checkbutton.
    bien_doc_sach = tk.BooleanVar(value=False)
    bien_the_thao = tk.BooleanVar(value=False)
    bien_am_nhac = tk.BooleanVar(value=False)
    tk.Checkbutton(
        cua_so, text="Doc sach", variable=bien_doc_sach
    ).pack(anchor="w", padx=30)

    tk.Checkbutton(
        cua_so, text="The thao", variable=bien_the_thao
    ).pack(anchor="w", padx=30)

    tk.Checkbutton(
        cua_so, text="Am nhac", variable=bien_am_nhac
    ).pack(anchor="w", padx=30)

    def xem_lua_chon():
        ket_qua = (
            f"Doc sach: {bien_doc_sach.get()}\n"
            f"The thao: {bien_the_thao.get()}\n"
            f"Am nhac: {bien_am_nhac.get()}"
        )
        nhan_ket_qua.config(text=ket_qua)

    tk.Button(
        cua_so,
        text="Xem lua chon",
        command=xem_lua_chon
    ).pack(pady=10)

    nhan_ket_qua = tk.Label(cua_so, text="", justify="left")
    nhan_ket_qua.pack()


# HOẠT ĐỘNG 2: RADIOBUTTON
def mo_cua_so_radiobutton():
    cua_so = tk.Toplevel(root)
    cua_so.title("Vi du Radiobutton")
    cua_so.geometry("320x220")
    bien_loai_tai_khoan = tk.StringVar(value="ca_nhan")

    tk.Label(
        cua_so,
        text="Chon loai tai khoan:",
        font=("Arial", 12)
    ).pack(pady=10)

    tk.Radiobutton(
        cua_so,
        text="Ca nhan",
        variable=bien_loai_tai_khoan,
        value="ca_nhan"
    ).pack(anchor="w", padx=30)

    tk.Radiobutton(
        cua_so,
        text="Doanh nghiep",
        variable=bien_loai_tai_khoan,
        value="doanh_nghiep"
    ).pack(anchor="w", padx=30)

    nhan_ket_qua = tk.Label(cua_so, text="")
    nhan_ket_qua.pack(pady=5)

    def xem_loai_tai_khoan():
        nhan_ket_qua.config(
            text=f"Ban da chon: {bien_loai_tai_khoan.get()}"
        )

    tk.Button(
        cua_so,
        text="Xac nhan",
        command=xem_loai_tai_khoan
    ).pack(pady=5)

root = tk.Tk()
root.title("Hoat dong 1 va 2")
root.geometry("360x180")

tk.Label(
    root,
    text="Thuc hanh Checkbutton va Radiobutton",
    font=("Arial", 11, "bold")
).pack(pady=15)

tk.Button(
    root,
    text="Mo vi du Checkbutton",
    command=mo_cua_so_checkbutton
).pack(pady=5)

tk.Button(
    root,
    text="Mo vi du Radiobutton",
    command=mo_cua_so_radiobutton
).pack(pady=5)

root.mainloop()
