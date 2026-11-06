import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import csdl_chi_tieu as db

DANH_SACH_THE_LOAI = ["Ăn uống", "Di chuyển", "Hóa đơn", "Mua sắm", "Giải trí", "Khác"]

class UngDungChiTieu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quản lý chi tiêu cá nhân")
        self.geometry("600x520")
        self.resizable(False, False)
        
        # Khởi tạo CSDL nếu chưa có
        db.tao_bang_neu_chua_co()
        
        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach()

    def khoi_tao_giao_dien(self):
        # --- Khung Nhập Liệu ---
        khung_nhap = tk.LabelFrame(self, text="Thêm khoản chi mới")
        khung_nhap.pack(pady=10, padx=10, fill="x")

        tk.Label(khung_nhap, text="Số tiến (VND):").grid(row=0, column=0, sticky="w", pady=5, padx=5)
        self.o_nhap_so_tien = tk.Entry(khung_nhap, width=30)
        self.o_nhap_so_tien.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Thể loại:").grid(row=1, column=0, sticky="w", pady=5, padx=5)
        self.chon_the_loai = ttk.Combobox(khung_nhap, values=DANH_SACH_THE_LOAI, width=27, state="readonly")
        self.chon_the_loai.current(0)
        self.chon_the_loai.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Ngày (DD/MM/YYYY):").grid(row=2, column=0, sticky="w", pady=5, padx=5)
        self.o_nhap_ngay = tk.Entry(khung_nhap, width=30)
        self.o_nhap_ngay.grid(row=2, column=1, padx=10, pady=5)

        tk.Latbel(khung_nhap, text="Ghi chú:").grid(row=3, column=0, sticky="w", pady=5, padx=5)
        self.o_nhap_ghi_chu = tk.Entry(khung_nhap, width=30)
        self.o_nhap_ghi_chu.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(khung_nhap, text="Thêm chi tiêu", command=self.xu_ly_them, bg="lightblue").grid(row=4, column=0, columnspan=2, pady=10)

        # --- Khung Danh Sách ---
        khung_danh_sach = tk.LabelFrame(self, text="Danh sách chi tiêu")
        khung_danh_sach.pack(pady=5, padx=10, fill="both", expand=True)

        self.listbox_chi_tieu = tk.Listbox(khung_danh_sach, width=80, height=12)
        self.listbox_chi_tieu.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        thanh_cuon = tk.Scrollbar(khung_danh_sach, orient="vertical", command=self.listbox_chi_tieu.yview)
        thanh_cuon.pack(side="right", fill="y", pady=5)
        self.listbox_chi_tieu.config(yscrollcommand=thanh_cuon.set)

        # --- Khung Thao Tác ---
        khung_nut_thao_tac = tk.Frame(self)
        khung_nut_thao_tac.pack(pady=10)

        tk.Button(khung_nut_thao_tac, text="Xóa khoản chi", command=self.xu_ly_xoa, bg="#ff9999").grid(row=0, column=0, padx=10)
        tk.Button(khung_nut_thao_tac, text="Thống kê chi tiêu", command=self.xu_ly_thong_ke, bg="#99ff99").grid(row=0, column=1, padx=10)

    def tai_lai_danh_sach(self):
        self.listbox_chi_tieu.delete(0, tk.END)
        self.danh_sach_hien_tai = db.lay_toan_bo_chi_tieu()
        for chi_tieu in self.danh_sach_hien_tai:
            id_ct, so_tien, the_loai, ngay, ghi_chu = chi_tieu
            # Format hiển thị
            chuoi_hien_thi = f"[{ngay}] {the_loai} - {so_tien:,.0f} VND - ({ghi_chu})"
            self.listbox_chi_tieu.insert(tk.END, chuoi_hien_thi)

    def xu_ly_them(self):
        so_tien_str = self.o_nhap_so_tien.get().strip()
        the_loai = self.chon_the_loai.get()
        ngay = self.o_nhap_ngay.get().strip()
        ghi_chu = self.o_nhap_ghi_chu.get().strip()
        
        # Xử lý lỗi nhập liệu
        if not so_tien_str or not ngay:
            messagebox.showerror("Lỗi", "Vui lòng nhập số tiền và ngày chi tiêu.")
            return
        
        try:
            so_tien = float(so_tien_str)
        except ValueError:
            messagebox.showerror("ỗi", "Số tiền phải là một con số hợp lệ.")
            return
        
        db.them_chi_tieu(so_tien, the_loai, ngay, ghi_chu)
        
        # Xóa trắng form nhập
        self.o_nhap_so_tien.delete(0, tk.END)
        self.o_nhap_ghi_chu.delete(0, tk.END)
        
        self.tai_lai_danh_sach()
        messagebox.showinfo("Thành công", "Đã thêm khoản chi mới.")

    def xu_ly_xoa(self):
        lua_chon = self.listbox_chi_tieu.curselection()
        if not lua_chon:
            messagebox.showerror("ỗi", "Vui lòng chọn một khoản chi trong danh sách để xóa.")
            return
        
        id_chi_tieu = self.danh_sach_hien_tai[lua_chon[0]][0]
        db.xoa_chi_tieu(id_chi_tieu)
        self.tai_lai_danh_sach()
        messagebox.showinfo("Thành công", "Đã xóa khoản chi.")

    def xu_ly_thong_ke(self):
        du_lieu_thong_ke = db.thong_ke_theo_the_loai()
        if not du_lieu_thong_ke:
            messagebox.showinfo("Thông báo", "Chưa có dữ liệu để thống kê.")
            return
        
        cac_the_loai = [dong[0] for dong in du_lieu_thong_ke]
        tong_tien = [dong[1] for dong in du_lieu_thong_ke]
        
        plt.figure(figsize=(7, 5))
        plt.bar(cac_the_loai, tong_tien, color="lightcoral")
        plt.title("Tổng Chi Tiêu Theo Thể Loại")
        plt.xlabel("Thể Loại")
        plt.ylabel("Tổng Tiền (VND)")
        
        # Định dạng hiển thị số tiền trên trục Y tránh bị lỗi font số lớn
        plt.ticklabel_format(style='plain', axis='y')
        
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    ung_dung = UngDungChiTieu()
    ung_dung.mainloop()