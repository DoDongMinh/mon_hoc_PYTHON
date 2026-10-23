import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

class MayTinhBoTui(QWidget):
    def __init__(self):
        super().__init__()
        # Tự động lấy đường dẫn và nạp file .ui
        duong_dan_hien_tai = os.path.dirname(__file__)
        file_ui = os.path.join(duong_dan_hien_tai, "caculator.ui")
        uic.loadUi(file_ui, self)
        
        self.bieu_thuc = ""
        self.khoi_tao_ket_noi()

    def khoi_tao_ket_noi(self):
        # Kết nối sự kiện cho các nút số từ 0 đến 9
        for i in range(10):
            nut = getattr(self, f"nut_{i}", None)
            if nut:
                nut.clicked.connect(lambda checked, val=str(i): self.them_ky_tu(val))

        if hasattr(self, 'nut_cong'):
            self.nut_cong.clicked.connect(lambda: self.them_ky_tu(" + "))
        if hasattr(self, 'nut_tru'):
            self.nut_tru.clicked.connect(lambda: self.them_ky_tu(" - "))
        if hasattr(self, 'nut_nhan'):
            self.nut_nhan.clicked.connect(lambda: self.them_ky_tu(" * "))
        if hasattr(self, 'nut_chia'):
            self.nut_chia.clicked.connect(lambda: self.them_ky_tu(" / "))
        if hasattr(self, 'nut_cham'):
            self.nut_cham.clicked.connect(lambda: self.them_ky_tu("."))

        if hasattr(self, 'nut_c'):
            self.nut_c.clicked.connect(self.xoa_man_hinh)
        if hasattr(self, 'nut_bang'):
            self.nut_bang.clicked.connect(self.tinh_ket_qua)

    def them_ky_tu(self, ky_tu):
        self.bieu_thuc += ky_tu
        self.man_hinh.setText(self.bieu_thuc)

    def xoa_man_hinh(self):
        self.bieu_thuc = ""
        self.man_hinh.clear()

    def tinh_ket_qua(self):
        try:
            ket_qua = str(eval(self.bieu_thuc))
            self.man_hinh.setText(ket_qua)
            self.bieu_thuc = ket_qua 
        except ZeroDivisionError:
            QMessageBox.critical(self, "Lỗi", "Không thể chia cho số 0!")
            self.xoa_man_hinh()
        except Exception:
            QMessageBox.critical(self, "Lỗi", "Biểu thức không hợp lệ!")
            self.xoa_man_hinh()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = MayTinhBoTui()
    cua_so.show()
    sys.exit(app.exec_())