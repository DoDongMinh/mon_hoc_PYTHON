import sqlite3

TEN_FILE_CSDL = "chi_tieu.db"

def ket_noi_csdl():
    return sqlite3.connect(TEN_FILE_CSDL)

def tao_bang_neu_chua_co():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("""
        CREATE TABLE IF NOT EXISTS chi_tieu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            so_tien REAL NOT NULL,
            the_loai TEXT NOT NULL,
            ngay_thang TEXT NOT NULL,
            ghi_chu TEXT
        )
    """)
    ket_noi.commit()
    ket_noi.close()

def them_chi_tieu(so_tien, the_loai, ngay_thang, ghi_chu):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute(
        "INSERT INTO chi_tieu (so_tien, the_loai, ngay_thang, ghi_chu) VALUES (?, ?, ?, ?)", 
        (so_tien, the_loai, ngay_thang, ghi_chu)
    )
    ket_noi.commit()
    ket_noi.close()

def lay_toan_bo_chi_tieu():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT id, so_tien, the_loai, ngay_thang, ghi_chu FROM chi_tieu ORDER BY id DESC")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua

def xoa_chi_tieu(id_chi_tieu):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("DELETE FROM chi_tieu WHERE id = ?", (id_chi_tieu,))
    ket_noi.commit()
    ket_noi.close()

def thong_ke_theo_the_loai():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    # Thống kê tổng số tiền thay vì đếm số lượng
    con_tro.execute("SELECT the_loai, SUM(so_tien) FROM chi_tieu GROUP BY the_loai")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua