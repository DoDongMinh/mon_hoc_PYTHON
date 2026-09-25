# HOẠT ĐỘNG 6: Đệ quy - Giai thừa, Fibonacci
# Bài tập 6.1 - Giai thừa bằng đệ quy
def giai_thua_de_quy(n):
    if n <= 1: # dieu kien dung
        return 1
    return n * giai_thua_de_quy(n - 1)

def giai_thua_lap(n):
    ket_qua = 1
    for i in range(1, n + 1):
        ket_qua *= i
    return ket_qua

print(giai_thua_de_quy(5), "-", giai_thua_lap(5))
# Yêu cầu: Sau khi thực hiện bằng đệ quy, hãy so sánh với vòng lặp việc sử dụng vòng lặp
'''
  Đệ quy (giai_thua_de_quy):
   - Ưu điểm: Mã nguồn ngắn gọn, thể hiện rõ bản chất công thức toán học.   
   - Nhược điểm: Tốn bộ nhớ bộ đệm Call Stack cho mỗi lần gọi hàm, nếu $n$ quá lớn sẽ tràn bộ nhớ (RecursionError) và tốc độ chậm hơn.   
  Vòng lặp (giai_thua_lap):
  - Ưu điểm: Hiệu năng cao hơn (độ phức tạp bộ nhớ $O(1)$), không nguy cơ bị đè đống Stack.   
  - Nhược điểm: Mã dài hơn một chút so với đệ quy.   
'''


# Bài tập 6.2 - Số Fibonacci thứ n bằng đệ quy
def fibonacci_de_quy(n):
    if n <= 1: # dieu kien dung
        return n
    return fibonacci_de_quy(n - 1) + fibonacci_de_quy(n - 2)

for i in range(10):
    print(fibonacci_de_quy(i), end=" ")
print()

# Yêu cầu: Thử tính fibonacci_de_quy(30), quan sát thời gian chạy chậm hơn hẳn so với
# giai_thua_de_quy(30), trả lời vì sao đệ quy Fibonacci "tốn kém" hơn (gợi ý: số lần gọi hàm tăng theo cấp số
# nhân do tính lại nhiều lần các giá trị trùng nhau).
'''
   - Nguyên nhân: Hàm đệ quy Fibonacci thông thường có độ phức tạp thời gian lên tới $O(2^n)$ (tăng theo cấp số nhân).   
   - Lý do cụ thể:Tính lại các giá trị trùng lặp: Để tính fibonacci(30), hàm gọi fibonacci(29) và fibonacci(28). Nhưng bản thân fibonacci(29) lại gọi lại 
   - fibonacci(28) và fibonacci(27). Việc này làm cho một giá trị (ví dụ fibonacci(5)) bị tính lặp đi lặp lại hàng triệu lần không cần thiết.   
   - Bùng nổ cây gọi hàm: Số lượng hàm đệ quy được gọi tăng theo cây nhị phân, gây lãng phí CPU và tràn bộ nhớ lưu trữ lời gọi hàm.   
'''
