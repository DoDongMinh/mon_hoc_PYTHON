#Câu hỏi: Với một dự án cần bàn giao cho khách hàng, giao diện phải chuyên nghiệp, nên chọn  Tkinter hay PyQt? Vì sao? 
'''
Nên chọn PyQt.
Lý do:
  - Thẩm mỹ và hiện đại: PyQt được xây dựng dựa trên bộ thư viện C++ Qt nổi tiếng, hỗ trợ sẵn hệ thống StyleSheet (tương tự CSS)
    giúp dễ dàng tùy biến giao diện, bo góc, đổi màu, tạo hiệu ứng chuyển động và hiển thị sắc nét trên các màn hình độ phân giải cao
    (High-DPI). Trong khi đó, giao diện mặc định của Tkinter mang phong cách cổ điển, thiếu tinh tế và cần rất nhiều thư viện phụ trợ nếu muốn 
    làm đẹp.
  - Hỗ trợ Qt Designer: Cung cấp công cụ thiết kế trực quan kéo - thả (Qt Designer), giúp rút ngắn đáng kể thời gian xây dựng các form phức tạp.
  - Hệ thống widget phong phú: PyQt cung cấp sẵn hàng loạt widget nâng cao phục vụ cho ứng dụng doanh nghiệp như QTableView, QTreeView, 
    QTabWidget, QCalendarWidget, QDockWidget, v.v.
'''
