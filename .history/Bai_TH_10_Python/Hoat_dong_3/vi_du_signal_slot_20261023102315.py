import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout

class ViDuSignalSlot(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vi du Signal - Slot")
        self.resize(300, 180)

        self.o_nhap = QLineEdit()
        nut_hien_thi = QPushButton("Hien thi noi dung")
        self.nhan_ket_qua = QLabel("Chua co noi dung")

        layout = QVBoxLayout()
        layout.addWidget(self.o_nhap)
        layout.addWidget(nut_hien_thi)
        layout.addWidget(self.nhan_ket_qua)
        self.setLayout(layout)

        # Bài tập 3.2: Kết nối một signal tới nhiều slot
        nut_hien_thi.clicked.connect(self.hien_thi_noi_dung)
        nut_hien_thi.clicked.connect(lambda: print("Nut vua duoc bam!"))

    def hien_thi_noi_dung(self):
        noi_dung = self.o_nhap.text()
        self.nhan_ket_qua.setText(f"Ban vua nhap: {noi_dung}")

app = QApplication(sys.argv)
cua_so = ViDuSignalSlot()
cua_so.show()
sys.exit(app.exec_())

#Yêu cầu: giải thích cụm từ "signal - slot" - clicked đóng vai trò signal (tín hiệu phát ra khi có sự kiện), còn hien_thi_noi_dung đóng 
# vai trò slot (hàm được gọi khi nhận tín hiệu đó). So sánh với  cách Tkinter chỉ dùng command=ten_ham. 
'''
Khái niệm "Signal - Slot":
  - Signal (Tín hiệu): Là thông báo phát ra từ một widget khi có một sự kiện xảy ra (ví dụ: nút được nhấn clicked, text thay đổi textChanged).
  - Slot (Khe cắm): Là hàm hoặc phương thức được thực thi tự động khi signal tương ứng được kích hoạt.

So sánh với command=ten_ham của Tkinter:
  - Tkinter: Sử dụng tham số command trên widget (chỉ hỗ trợ một hàm duy nhất) hoặc phương thức .bind(). Việc truyền tham số phức tạp đòi hỏi 
    phải sử dụng thêm lambda hoặc functools.partial.
  - PyQt: Cơ chế signal.connect(slot) linh hoạt hơn rất nhiều, cho phép một signal kết nối tới nhiều slot (như Bài tập 3.2) hoặc nhiều signal 
    cùng kết nối tới một slot, hỗ trợ kiểm tra kiểu dữ liệu chặt chẽ và truyền tham số trực tiếp qua các signal có sẵn.
'''
