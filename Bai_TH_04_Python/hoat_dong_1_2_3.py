#HOẠT ĐỘNG 1
#Bài tập 1.1 - Khai báo truy xuất
sinh_vien = {
    "ho_ten": "Nguyen Van A",
    "nam_sinh": 2004,
    "diem_tb": 8.5
}
print(sinh_vien["ho_ten"]) 
print(sinh_vien.get("diem_tb")) 
print(sinh_vien.get("lop", "Chua co"))

#Yêu cầu: Giải thích vì sao dùng sinh_vien["lop"] (khi "lop" chưa tồn tại) sẽ gây lỗi KeyError, còn
#sinh_vien.get("lop", "Chua co") thì không.
"""
dictionary sinh_vien chỉ có các khóa như "ho_ten", "nam_sinh" và "diem_tb", chưa có khóa "lop".
  Khi sử dụng cách truy xuất:

       sinh_vien["lop"]

  Python sẽ yêu cầu dictionary phải có chính xác khóa "lop". Vì khóa này chưa tồn tại nên Python không biết phải lấy giá trị nào và phát sinh lỗi KeyError.

  Trong khi đó, phương thức: sinh_vien.get("lop", "Chua co") có cách hoạt động an toàn hơn. Nó tìm khóa "lop" trong dictionary. Nếu tìm thấy thì trả về giá trị tương ứng; nếu không tìm thấy, nó sẽ trả về giá trị mặc định "Chua co" thay vì báo lỗi.
  Vì vậy, với trường hợp "lop" chưa tồn tại, kết quả sẽ là: "Chua co"

Kết luận: dict["key"] phù hợp khi chắc chắn khóa tồn tại, còn dict.get("key", giá_trị_mặc_định) phù hợp khi có khả năng khóa chưa tồn tại và muốn chương trình tiếp tục chạy bình thường.
"""

#Bài tập 1.2 - Thêm/sửa/xóa:
sinh_vien["lop"] = "CNTT01" 
sinh_vien["diem_tb"] = 9.0 
print(sinh_vien)
diem_cu = sinh_vien.pop("diem_tb") 

print(sinh_vien, "- diem da xoa:", diem_cu)
sinh_vien.update({"nam_sinh": 2003, "email": "a@example.com"}) 
print(sinh_vien)

#HOẠT ĐỘNG 2 Duyệt Dictionary bằng for - keys/values/items
diem_mon_hoc = {"Toan": 8.0, "Ly": 7.5, "Hoa": 9.0, "Van": 6.5}
for mon in diem_mon_hoc.keys():
    print(mon)
for diem in diem_mon_hoc.values():
    print(diem)
for mon, diem in diem_mon_hoc.items():
    print(f"{mon}: {diem}")
    
tong_diem = 0
for diem in diem_mon_hoc.values():
    tong_diem = tong_diem + diem

print("Diem trung binh:", round(tong_diem / len(diem_mon_hoc), 2))

#HOẠT ĐỘNG 3: Dictionary comprehension & giới thiệu Set
#Bài tập 3.1 - Dictionary comprehension:
diem_mon_hoc = {"Toan": 8.0, "Ly": 7.5, "Hoa": 9.0, "Van": 6.5}
diem_cong_diem = {mon: round(diem + 0.5, 2) for mon, diem in diem_mon_hoc.items()}
print(diem_cong_diem)

ten_mon_viet_hoa = {mon.upper(): diem for mon, diem in diem_mon_hoc.items()}
print(ten_mon_viet_hoa)

#Bài tập 3.2 - So sánh nhanh với Set:
mon_hoc_ky1 = {"Toan", "Ly", "Hoa", "Van"}
mon_hoc_ky2 = {"Toan", "Anh", "Tin", "Van"}
print(mon_hoc_ky1 & mon_hoc_ky2) 
print(mon_hoc_ky1 | mon_hoc_ky2) 
#Yêu cầu:So sánh Set với Dictionary - Set có lưu cặp khóa-giá trị không? Vì sao Set không cho phép phần tử trùng lặp?
"""
 - Set và Dictionary đều là kiểu dữ liệu dùng để lưu nhiều phần tử, nhưng cách tổ chức dữ liệu của chúng khác nhau.
   Dictionary lưu dữ liệu theo dạng khóa – giá trị (key – value). Mỗi khóa dùng để xác định và truy xuất một giá trị tương ứng. Ví dụ, thông tin sinh viên có thể lưu tên, năm sinh, điểm trung bình,... thông qua các khóa.
 - Ngược lại, Set chỉ lưu các phần tử, không tổ chức dữ liệu thành cặp khóa – giá trị. Ví dụ một Set các môn học có thể chứa "Toan", "Ly", "Hoa", "Van".
   Đặc điểm quan trọng của Set là các phần tử không được trùng nhau. Nếu ta đưa cùng một phần tử vào Set nhiều lần thì Set vẫn chỉ giữ lại một phần tử đó.
   Ví dụ, nếu có các môn:

       Toan, Ly, Toan, Hoa

   thì Set chỉ lưu:

       Toan, Ly, Hoa
       
 - Lý do là Set được thiết kế để biểu diễn một tập hợp các phần tử duy nhất, nên nó tự động loại bỏ các phần tử bị trùng.
   Đây cũng là lý do Set rất hữu ích khi cần loại bỏ dữ liệu trùng lặp hoặc thực hiện các phép toán tập hợp như giao, hợp và hiệu.

"""
