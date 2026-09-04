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
print("Python", "la", "ngon", "ngu", "lap trinh", sep="0")
print("Dong 1", end=" | ")
print("Dong 2") 
#thử đổi sep thành nhiều ký tự khác nhau (", ", "\n") và quan sát kết quả rồi giải thích.
'''
  sep="-" : In ra "Python-la-ngon-ngu-lap trinh"  
  sep="," : In ra "Python,la,ngon,ngu,lap trinh"
  sep="\n" : In ra" Python
                    la
                    ngon
                    ngu
                    lap trinh "
'''
