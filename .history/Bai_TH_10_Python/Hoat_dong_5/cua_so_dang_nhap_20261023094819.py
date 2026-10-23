import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox  
class CuaSoDangNhap(QDialog): 
    def __init__(self):
        super().__init__()
        duong_dan_hien_tai = os.path.dirname(__file__)
        file_ui = os.path.join(duong_dan_hien_tai, "form_dang_nhap.ui")
        
        uic.loadUi(file_ui, self)
        self.nut_dang_nhap.clicked.connect(self.xu_ly_dang_nhap)

    def xu_ly_dang_nhap(self):
        tai_khoan = self.o_nhap_tai_khoan_2.text()
        mat_khau = self.o_nhap_mat_khau.text()
        if tai_khoan == "" or mat_khau == "":
            QMessageBox.critical(self, "Loi", "Vui long nhap day du tai khoan va mat khau.")
            return
        QMessageBox.information(self, "Thanh cong", f"Xin chao {tai_khoan}, dang nhap thanh cong!")
app = QApplication(sys.argv)
cua_so = CuaSoDangNhap()
cua_so.show()
sys.exit(app.exec_())