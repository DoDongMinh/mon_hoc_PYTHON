danh_sach_sv = [(8.5, "An"), (7.0, "Binh"), (9.2, "Chi"), (6.5, "Dung")]

#Thêm sinh viên mới
danh_sach_sv.append((8.0, "Em"))

#Xóa 1 sinh viên
danh_sach_sv.remove((7.0, "Binh"))

#Sửa điểm cho sinh viên ở vị trí xác định(ví dụ ở vị trí 0)
danh_sach_sv[0] = (9.0, danh_sach_sv[0][1])

#Kiểm tra một sinh viên có trong danh sách hay không
print("Chi co trong danh sach khong?", (9.2, "Chi") in danh_sach_sv)

#Sắp xếp theo điểm tăng dần
danh_sach_sv.sort()
print("Danh sach sau khi sap xep theo diem tang dan: ")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")
    
#Sắp xếp theo điểm giảm dần
danh_sach_sv.sort(reverse=True)
print("Danh sach sau khi sap xep theo diem giam dan:")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")