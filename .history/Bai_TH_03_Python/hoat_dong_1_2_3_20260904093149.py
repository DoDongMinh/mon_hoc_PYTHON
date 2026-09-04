# HOẠT ĐỘNG 1
#Bài tập 1.1 - Khai báo & truy cập:
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]

print(diem_so[0])      
print(diem_so[-1])     
print(diem_so[1:4])    
print(diem_so[::2])    
print(diem_so[::-1])  

#Bài tập 1.2: Các phương thức thường dùng
ten_sv = ["An", "Binh", "Chi"]

ten_sv.append("Dung")          
ten_sv.insert(1, "Em")         
print(ten_sv)

ten_sv.remove("Chi")           
pop_ra = ten_sv.pop()          
print(ten_sv, "- da xoa:", pop_ra)

ten_sv.sort()                  
print(ten_sv)
ten_sv.reverse()               
print(ten_sv)

ten_sv.extend(["Giang", "Hoa"]) 
print(ten_sv)

#Yêu cầu: Giải thích sự khác nhau giữa remove() và pop()
'''
 - remove(x): Xóa phần tử dựa trên giá trị x xuất hiện đầu tiên trong danh sách. 
   Lệnh này không trả về giá trị (trả về None). Nếu giá trị không tồn tại sẽ gây lỗi ValueError.

-- pop(): Xóa phần tử dựa trên chỉ số (vị trí) i (mặc định xóa phần tử cuối nếu không truyền i). 
   Lệnh này trả về giá trị của phần tử vừa bị xóa.
'''

#HOẠT ĐỘNG 2
#Bài tập 2.1 - Duyệt list bằng for:
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
tong = 0

for diem in diem_so:
    print(diem)
    tong = tong + diem

print("Tong diem:", tong)
print("Diem trung binh:", round(tong / len(diem_so), 2))

#Bài tập 2.2 - List lồng nhau (ma trận):
ma_tran = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for hang in ma_tran:
    print(hang)

for hang in ma_tran:
    for phan_tu in hang:
        print(phan_tu, end=" ")
    print()
  
#Yêu cầu: Viết thêm đoạn code tính tổng tất cả phần tử trong ma_tran bằng cách dùng biến tổng cộng dồn qua 2 vòng for lồng nhau.
tong_ma_tran = 0
for hang in ma_tran:
    for phan_tu in hang:
        tong_ma_tran += phan_tu
print("Tong tat ca phan tu trong ma tran:", tong_ma_tran)

#HOẠT ĐỘNG 3
#Bài tập 3.1 - Lọc số chẵn/lẻ:
day_so = list(range(1, 21))  # day so tu 1 den 20

so_chan = [x for x in day_so if x % 2 == 0]
so_le = [x for x in day_so if x % 2 != 0]

print("So chan:", so_chan)
print("So le:", so_le)

#Bài tập 3.2 - Biến đổi phần tử:
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
diem_cong = [round(diem + 0.5, 2) for diem in diem_so]
print(diem_cong)
