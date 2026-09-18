#HOẠT ĐỘNG 4: Chuyển đổi kiểu dữ liệu tường minh & ngầm định
chuoi_so = "25"
so = int(chuoi_so)
print(so, type(so))
so_thuc = float("3.14")
print(so_thuc, type(so_thuc))
danh_sach = list((1, 2, 3)) 
bo_ba = tuple([4, 5, 6]) 
tap_hop = set([1, 2, 2, 3, 3, 3]) 
tu_dien = dict([("a", 1), ("b", 2)])
print(danh_sach, bo_ba, tap_hop, tu_dien)

#Bài tập 4.2 - Trường hợp gây lỗi khi ép kiểu:
so_hop_le = int(float("3.14")) # cach lam dung: ep qua float truoc
print(so_hop_le)

#Bài tập 4.3 - Chuyển đổi ngầm định:
ket_qua = 5 + 2.5 
print(ket_qua, type(ket_qua))
ket_qua_2 = "Diem: " + str(8.5)
print(ket_qua_2)
