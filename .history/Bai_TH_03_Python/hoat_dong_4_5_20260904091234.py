#HOẠT ĐỘNG 4
#Bài tập 4.1 - Khai báo & tính bất biến:
toa_do = (3, 5)
print(toa_do, type(toa_do))

#Bài tập 4.2 - Unpacking tuple:
x, y = toa_do
print("x =", x, "- y =", y)

a, b = 10, 20
a, b = b, a
print("a =", a, "- b =", b)

#Bài tập 4.3 - Trả về nhiều giá trị từ một biểu thức:
c, d = 17, 5
thuong_du = divmod(c, d)     
thuong, du = thuong_du     
print(f"{c} chia {d} duoc thuong {thuong}, du {du}")

#HOẠT ĐỘNG 5
import math

diem_a = (2, 3)
diem_b = (7, 8)

xa, ya = diem_a
xb, yb = diem_b

khoang_cach = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
print(f"Khoang cach giua {diem_a} va {diem_b} la: {round(khoang_cach, 2)}")

#Yêu cầu: Tạo thêm danh sách cac_diem = [(0,0), (3,4), (6,8)] (list chứa các tuple tọa độ), dùng for để in ra khoảng cách của từng điểm so với gốc tọa độ (0, 0).
cac_diem = [(0, 0), (3, 4), (6, 8)]
goc_toa_do = (0, 0)
x0, y0 = goc_toa_do

for diem in cac_diem:
    x, y = diem
    kc = math.sqrt((x - x0) ** 2 + (y - y0) ** 2)
    print(f"Khoang cach tu diem {diem} den goc toa do {goc_toa_do} la: {round(kc, 2)}")