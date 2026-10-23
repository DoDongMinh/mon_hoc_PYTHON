import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class CuaSoDauTien(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cua so PyQt dau tien")
        self.resize(300, 200)

        layout = QVBoxLayout()
        nhan = QLabel("Xin chao PyQt!")
        layout.addWidget(nhan)
        self.setLayout(layout)

app = QApplication(sys.argv)
cua_so = CuaSoDauTien()
cua_so.show()
sys.exit(app.exec_())

#Yêu cầu: so sánh nhanh cấu trúc trên với cua_so = tk.Tk() + mainloop() của Tkinter — app.exec_() đóng vai trò tương tự mainloop() như thế nào?
'''
So sánh app.exec_() với root.mainloop() của Tkinter:
  - Điểm tương đồng: Cả hai đều khởi động vòng lặp sự kiện chính (Event Loop) của ứng dụng giao diện đồ họa. Vòng lặp này chạy liên 
    tục để lắng nghe các tác động từ người dùng (như click chuột, gõ bàn phím, thay đổi kích thước cửa sổ) và thực thi các phản hồi tương 
    ứng, đồng thời giữ cho cửa sổ hiển thị không bị tắt đột ngột.
  - Điểm khác biệt: Trong Tkinter, vòng lặp gắn liền với cửa sổ gốc (root.mainloop()), trong khi trong PyQt, vòng lặp quản lý toàn bộ phiên ứng
    dụng thông qua đối tượng QApplication (app.exec_()).
'''
