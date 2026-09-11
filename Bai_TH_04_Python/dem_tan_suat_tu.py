# HOẠT ĐỘNG 6: Vận dụng - Đếm tần suất từ trong văn bản

doan_van = "python la ngon ngu lap trinh python de hoc python de dung"
danh_sach_tu = doan_van.split()
tan_suat = {}
for tu in danh_sach_tu:
    tan_suat[tu] = tan_suat.get(tu, 0) + 1
print("Tan suat xuat hien cac tu:")
for tu, so_lan in tan_suat.items():
    print(f"{tu}: {so_lan}")

#Yêu cầu: Giải thích cách hoạt động của tan_suat.get(tu, 0) + 1 - vì sao chỉ một dòng này đã thay thế được việc phải kiểm tra "từ đã xuất hiện hay chưa".
"""
 - Trong bài toán, tan_suat là một dictionary dùng để đếm số lần mỗi từ xuất hiện trong đoạn văn.
   Khi duyệt từng từ, ta cần biết từ đó đã xuất hiện trước đó hay chưa.
   Thông thường, nếu viết đầy đủ, ta phải kiểm tra:
    + Nếu từ đã có trong dictionary → tăng số lần xuất hiện lên 1.
    + Nếu từ chưa có → tạo khóa mới và cho số lần xuất hiện bằng 1.
 - Phương thức .get() giúp thực hiện việc này ngắn gọn hơn.
   Cụ thể:

       tan_suat.get(tu, 0)

   có nghĩa là: lấy số lần xuất hiện của từ tu; nếu từ này chưa tồn tại thì coi số lần xuất hiện hiện tại là 0.
 - Sau đó cộng thêm 1 để ghi nhận lần xuất hiện mới:

       tan_suat.get(tu, 0) + 1

 - Ví dụ, lần đầu gặp từ "python", vì "python" chưa có trong tan_suat nên .get() trả về 0. Cộng thêm 1 thì số lần xuất hiện của "python" trở thành 1.
   Khi gặp "python" lần thứ hai, lúc này dictionary đã có "python": 1. .get() lấy ra 1, cộng thêm 1 thành 2.
 - Tương tự, lần thứ ba sẽ thành 3. Như vậy, dòng lệnh:

       tan_suat[tu] = tan_suat.get(tu, 0) + 1

   đã kết hợp cả kiểm tra và tăng số lần xuất hiện trong một câu lệnh.
    
"""