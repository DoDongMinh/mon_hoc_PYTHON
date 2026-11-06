#Câu hỏi: Nếu muốn xây dựng một hệ thống "chatbot tư vấn tuyển sinh" hoàn chỉnh, cần kết hợp những  thư viện nào trong bảng trên (gợi ý: cần cả phần "bộ não" xử lý 
# ngôn ngữ lẫn phần "giao diện" để người  dùng truy cập)? 
'''
 Để xây dựng hệ thống chatbot hoàn chỉnh, ta cần kết hợp 2 nhóm thư viện:
   - Phần "Bộ não" (Xử lý ngôn ngữ tự nhiên - NLP): Sử dụng TensorFlow hoặc PyTorch để xây dựng, huấn luyện và chạy các mô hình 
     học sâu (Deep Learning) giúp hiểu và sinh ra phản hồi ngôn ngữ.   
   - Phần "Giao diện/Giao tiếp" (Web Server/API): Sử dụng FastAPI (để xây dựng API tốc độ cao kết nối với mô hình AI) hoặc Flask/Django
     để tạo web server xử lý các yêu cầu (requests) từ người dùng cuối và trả về tin nhắn của chatbot. Ngoài ra, có thể dùng thêm Requests 
     nếu hệ thống cần gọi API của các nền tảng nhắn tin bên ngoài (như Zalo, Messenger, Telegram).   
'''
