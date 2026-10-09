**Hoạt động 3: Phân tích đề bài & thiết kế đồ án**
**Đề bài: "Quản lý thư viện"**

**Bước 1 – Xác định chức năng cần có:**

1. Hiển thị danh sách toàn bộ sách (mã sách, tên sách, tác giả, thể loại, số lượng, số lượng còn).
2. Xem nhanh các sách đang có sẵn để cho mượn.
3. Thêm sách mới vào thư viện.
4. Cho mượn sách cho độc giả (giảm số lượng sách có sẵn).
5. Trả sách (tăng lại số lượng sách có sẵn).
6. Tìm kiếm sách theo mã sách hoặc tên sách.
7. Thống kê số lượng sách và tình trạng mượn/trả.

**Bước 2 – Chọn cấu trúc dữ liệu lưu trữ:**
• Mỗi sách là một dict: `{"ma_sach", "ten_sach", "tac_gia", "the_loai", "so_luong", "so_luong_co_san"}`.
• Toàn bộ sách lưu trong một list các dict — phù hợp vì số lượng sách có thể thay đổi khi thêm sách và mỗi sách có nhiều thuộc tính khác kiểu nhau.
• Lịch sử mượn/trả lưu trong một list các dict riêng để theo dõi các giao dịch và phục vụ thống kê.

**Bước 3 – Chia nhỏ thành các hàm:** mỗi chức năng ở Bước 1 tương ứng với một hàm riêng, cộng thêm 1 hàm hỗ trợ nhập số nguyên an toàn bằng try-except, và 1 hàm chạy vòng lặp menu chính.
