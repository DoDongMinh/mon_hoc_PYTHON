# Bài tập 1.1 -input() và ép kiểu
ho_ten = input("Nhap ho ten: ")
nam_sinh = int(input("Nhap nam sinh: "))
diem_tb = float(input("Nhap diem trung binh: "))
#giải thích vì sao phải ép kiểu int()/float() cho nam_sinh và diem_tb, trong khi ho_ten thì không cần.
print("Python", "la", "ngon", "ngu", "lap trinh", sep="-")
'''
1. Với ho_ten (Không cần ép kiểu)

 -Họ tên bản chất đã là dạng văn bản (chuỗi ký tự).

 -Do input() mặc định trả về kiểu chuỗi (str), kết quả nhận được đã đúng ngay mục đích sử dụng nên không cần thực hiện ép kiểu.

2. Với nam_sinh (Phải ép sang int)

 -Khi nhập 2004, hàm input() sẽ nhận vào chuỗi "2004" (chữ số, không phải số).

 -Cần ép sang kiểu số nguyên (int) để thực hiện các phép toán đại số (ví dụ: tính tuổi bằng công thức 2026 - nam_sinh). Nếu để nguyên kiểu chuỗi, Python sẽ báo lỗi khi lấy số trừ cho chuỗi.

3. Với diem_tb (Phải ép sang float)

 -Ví dụ Khi nhập 8.5, hàm input() sẽ nhận vào chuỗi "8.5".

 -Điểm trung bình thường chứa số thập phân, nên cần ép sang kiểu số thực (float) để phục vụ các phép toán hoặc so sánh logic (ví dụ: diem_tb >= 8.0 để xếp loại học lực).
'''
# Bài tập 1.2 -print() với sep/end
print("Python", "la", "ngon", "ngu", "lap trinh", sep=", ")
print("Dong 1", end=" | ")
print("Dong 2") 
#thử đổi sep thành nhiều ký tự khác nhau (", ", "\n") và quan sát kết quả rồi giải thích.
''' 
  sep="," : In ra " Python,la,ngon,ngu,lap trinh "
   - Giải thích: Dấu phẩy , được chèn vào giữa từng từ, làm các từ tách biệt.
  sep="'" : In ra " Python, la, ngon, ngu, lap trinh "
   - Giải thích: Dấu phẩy và khoảng trắng ,  được chèn vào giữa từng từ, giúp các từ tách biệt rõ ràng, dễ đọc như danh sách.
  sep="\n" : In ra" Python
                    la
                    ngon
                    ngu
                    lap trinh "
   - Giải thích: \n là ký tự điều khiển xuống dòng (newline). Khi đặt sep="\n", mỗi giá trị sẽ được in trên một dòng riêng biệt.                    
'''
# Bài tập 1.3 - So sánh 3 cách định dạng chuỗi
# f-string
print(f"Ho ten: {ho_ten} - Nam sinh: {nam_sinh} - DTB: {diem_tb: .2f}")

# str.format
print("Ho ten: {} - Nam sinh: {} - DTB: {:.2f}".format(ho_ten, nam_sinh, diem_tb))

# toán tử %
print("Ho ten: %s - Nam sinh: %d - DTB: %.2f" % (ho_ten, nam_sinh, diem_tb))
# 3 cách trên cho kết quả giống nhau, vậy vì sao Python hiện nay khuyến khích dùng f-string hơn?
'''
1. Cú pháp ngắn gọn, dễ đọc và dễ bảo trì

 - f-string: Biến được điền trực tiếp vào vị trí cần hiển thị, giúp code trực quan, nhìn vào là biết ngay dữ liệu nào sẽ nằm ở đâu.

 - str.format() và %: Phải liệt kê chuỗi biến ở cuối câu. Với các chuỗi dài hoặc nhiều biến, bạn rất dễ đếm nhầm thứ tự truyền vào hoặc nhầm lẫn giữa các vị trí {} hay %s.

2. Tốc độ thực thi nhanh nhất

 - f-string được xử lý ngay ở bước biên dịch (runtime evaluation) chứ không phải qua phương thức nối chuỗi hay phân tích định dạng thông thường, giúp hiệu năng tính toán nhanh hơn đáng kể so với 2 cách còn lại.

3. Cho phép tính toán và gọi hàm trực tiếp bên trong {}

 - f-string cho phép nhúng trực tiếp biểu thức toán học, hàm hoặc phương thức vào trong dấu {}:
'''

# HOẠT DỘNG 2: Chú thích & các kiểu trích dẫn
# Bài tập 2.1 - Chú thích
"""
Chu thich/docstring nhieu dong:
Chuong trinh quan ly diem sinh vien - Buoi 2
"""
ho_ten = "Do Dong Minh" # Bien luu ho ten

# Bài tập 2.2 - Các kiểu trích dẫn & escape
s1 = 'Xin chao'
s2 = "Ban co khoe khong?"
s3 = '''Day la
mot chuoi
nhieu dong'''
s4 = "Duong dan: C:\\Python\\data"
s5 = r"Duong dan raw: C:\Python\data"
s6 = "Ten toi la \"Minh\", con ban ten gi?"

print(s1); print(s2); print(s3); print(s4); print(s5); print(s6)
# giải thích khác biệt giữa s4 và s5 (raw string dùng khi nào?).
'''
1. Khác biệt giữa s4 và s5

 - Chuỗi s4 (Sử dụng Escape Character):

 - Cú pháp: "Duong dan: C:\\Python\\data"

 - Giải thích: Trong chuỗi thông thường, dấu gạch chéo ngược \ được xem là ký tự điều khiển (Escape character) kết hợp với ký tự sau nó để tạo ra ký tự đặc biệt (như \n là xuống dòng, \t là dấu tab). Vì vậy, để in ra một dấu \, bạn bắt buộc phải gõ hai dấu \\.

 - Chuỗi s5 (Sử dụng Raw String - Chuỗi nguyên bản):

 - Cú pháp: r"Duong dan raw: C:\Python\data" (có tiền tố r hoặc R đằng trước)

 - Giải thích: Khi thêm ký tự r ở đầu, Python sẽ coi chuỗi này là nguyên bản và vô hiệu hóa tất cả các chức năng của ký tự escape (\). Dấu \ trong s5 được hiểu thuần túy là ký tự dấu gạch chéo ngược bình thường mà không cần gõ double \\.

2. Raw String (r"...") được dùng khi nào?

 - Raw string đặc biệt hữu ích và được khuyến khích dùng trong các trường hợp chứa nhiều dấu \:

  + Đường dẫn thư mục trên Windows:
  + Đường dẫn Windows sử dụng dấu \. Nếu không dùng raw string, một đường dẫn như C:\new_folder\test sẽ bị hiểu nhầm: \n biến thành xuống dòng, \t biến thành dấu tab, gây ra lỗi đọc file.

 - Nên dùng: r"C:\new_folder\test"

  + Biểu thức chính quy (Regular Expressions - Regex):
  + Các mẫu regex dùng rất nhiều dấu \ (ví dụ: \d+, \w+, \s+). Dùng raw string giúp câu lệnh ngắn gọn, dễ đọc, không bị "rác" code do phải gõ hai lần \\.

 - Nên dùng: re.findall(r"\d+", text)

  + Chuỗi ký tự đặc biệt trong LaTeX hoặc HTML/XML parsing.
'''

