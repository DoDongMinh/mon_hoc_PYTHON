#HOẠT ĐỘNG 3: Number - int, float, complex & hàm built-in
# Bài tập 3.1 - Các kiểu số & chuyển đổi:
a = -7
b = 2.6789
c, d = 17, 5

print(abs(a))        # Giá trị tuyệt đối
print(round(b))      # làm tròn
print(round(b, 2))   # làm tròn 2 chữ số thập phân
print(pow(c, 2))     # c mũ 2
print(divmod(c, d))  # trả về (thương, dư) dạng tuple
#so sánh pow(c, 2) với c ** 2 (toán tử đã học ở Buổi 1) - hai cách này có luôn cho kết quả giống nhau không? Tại sao?
'''
 - Với các bài toán lũy thừa cơ bản, kết quả của cả 2 cách pow(c, 2) và c ** 2 là hoàn toàn giống nhau. Tuy nhiên chúng lại 
   khác nhau trong bản chất vận hành
 - Sự khác nhau: 
   1. Khác biệt về tham số (Tính năng mở rộng của pow())
     - c ** 2: Chỉ nhận đúng 2 số hạng (Cơ số và Số mũ).
     - pow(c, d, z): Hỗ trợ truyền vào tham số thứ 3 để thực hiện phép chia lấy dư sau khi tính số mũ (c ** d) % z
   2. Khác biệt về bản chất thực thi
     - c ** 2: Là một Toán tử (Operator) của Python. Nó được thực thi trực tiếp bằng các lệnh Bytecode ở
       mức thấp (BINARY_POWER), nên khi thực hiện các phép tính đơn giản, toán tử ** thường chạy nhanh hơn một chút so với hàm pow().
     - pow(c, 2): Là một Hàm tích hợp sẵn (Built-in Function). Khi gọi pow(), Python phải tốn thêm một bước giải nghĩa cuộc gọi hàm (function call overhead).  
   3. Khác biệt khi làm việc với thư viện ngoài (Numpy, Pandas, OOP)
     - Khi tự viết Lớp (Class) hoặc dùng các thư viện như Math, Numpy:
     - Toán tử ** sẽ gọi phương thức đặc biệt __pow__().
     - Hàm pow() tùy trường hợp có thể hành xử khác nếu lớp đó ghi đè (override) hoặc nếu bạn dùng math.pow().
       (Lưu ý: math.pow(c, 2) sẽ luôn ép kết quả về kiểu số thực float là 289.0, trong khi c ** 2 trả về số nguyên int 289).  
'''

# Bài tập 3.3 - Vận dụng: Tính nghiệm phương trình bậc hai (trường hợp có 2 nghiệm phân biệt):
#Cho phương trình a*x^2 + b*x + c = 0 với bộ số đã chọn trước sao cho delta luôn dương (ví dụ
# a=1, b=-3, c=2):
import math

a, b, c = 1, -3, 2
delta = b ** 2 -4 * a * c
x1 = (-b + math.sqrt(delta) / (2 * a))
x2 = (-b - math.sqrt(delta) / (2 * a))

print(f"Delta = {delta}")
print(f"Nghiem x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")

# HOẠT ĐỘNG 4: String - indexing, slicing & phương thức xử lý
#Bài tập 4.1 - Indexing & slicing:
cau = "lap trinh Python rat thu vi"

print(cau[0])
print(cau[-1])
print(cau[4:10])
print(cau[:8])
print(cau[11:])
print(cau[::-1])
# dùng cau[::-1] để in ra chuỗi đảo ngược, sau đó kiểm tra xem cau có phải là palindrome không bằng biểu thức so sánh: cau == cau[::-1].
# kiểm tra 
is_palindrome = (cau == cau[::-1])

print("Chuỗi đảo ngược: ", cau[::-1])
print("Có phải Palindrome không?: ", is_palindrome)
'''
Kết quả:
 - cau[::-1] cho ra: "iv uht tar nohtyP hnirt pal"
 - cau == cau[::-1] sẽ trả về: False
'''

# Bài tập 4.2 - Tính bất biến (immutable):
ten = "Minh"
ten_moi = "T" + ten[1:]
print(ten_moi)

