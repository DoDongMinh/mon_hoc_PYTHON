import utils

print(utils.dao_nguoc_chuoi("Python"))
print(utils.kiem_tra_palindrome("madam"))
print(utils.chuan_hoa_ho_ten("  nguyen   van   an  "))
print(utils.uscln(24, 36))
print(utils.kiem_tra_nguyen_to(29))
# Yêu cầu: Giải thích vì sao utils.py và main.py cần đặt trong cùng một thư mục để lệnh import utils hoạt động đúng.
'''
   - Khi thực thi import utils, Python sẽ tìm kiếm file utils.py theo thứ tự nằm trong sys.path.   
   - Thư mục chứa file script đang chạy (main.py) mặc định chính là đường dẫn đầu tiên được thêm vào danh sách sys.path.   
   - Việc đặt utils.py và main.py trong cùng thư mục đảm bảo cho trình thông dịch của Python tìm thấy file utils.py ngay lập tức mà 
     không gặp lỗi ModuleNotFoundError: No module named 'utils'.   
'''
