# HOẠT ĐỘNG 1
#Bài tập 1.1 - if đơn và if-else:
tuoi = 20

if tuoi >= 18:
    print("Da du tuoi truong thanh")

if tuoi >= 18:
    print("Duoc phep dang ky xe may")
else:
    print("Chua du tuoi")

#Bài tập 1.2 – if-elif-else:
diem = 7.2

if diem >= 8.0:
    print("Xep loai: Gioi")
elif diem >= 6.5:
    print("Xep loai: Kha")
elif diem >= 5.0:
    print("Xep loai: Trung binh")
else:
    print("Xep loai: Yeu")
    
#Bài tập 1.3 – Điều kiện lồng nhau:
tuoi = 17
co_giay_phep = False

if tuoi >= 18:
    if co_giay_phep:
        print("Duoc phep lai xe")
    else:
        print("Du tuoi nhung chua co giay phep")
else:
    print("Chua du tuoi lai xe")
    
#Bài tập 1.4 – Biểu thức điều kiện rút gọn (conditional expression):
diem = 4.5
ket_qua = "Dat" if diem >= 5.0 else "Khong dat"
print(ket_qua)

so = -7
tri_tuyet_doi = so if so >= 0 else -so
print(tri_tuyet_doi)

# HOẠT ĐỘNG 2
#Bài tập 2.1 – Xếp loại học lực đầy đủ:
ho_ten = "Nguyen Van A"
diem_toan, diem_ly, diem_hoa = 8.0, 7.5, 9.0

dtb = round((diem_toan + diem_ly + diem_hoa) / 3, 2)

if dtb >= 8.0:
    xep_loai = "Gioi"
elif dtb >= 6.5:
    xep_loai = "Kha"
elif dtb >= 5.0:
    xep_loai = "Trung binh"
else:
    xep_loai = "Yeu"

print(f"{ho_ten} - DTB: {dtb} - Xep loai: {xep_loai}")

#Bài tập 2.2 – Tìm số lớn nhất trong 3 số nhập vào:
a = float(input("Nhap so thu nhat: "))
b = float(input("Nhap so thu hai: "))
c = float(input("Nhap so thu ba: "))

if a >= b and a >= c:
    lon_nhat = a
elif b >= a and b >= c:
    lon_nhat = b
else:
    lon_nhat = c

print("So lon nhat la:", lon_nhat)