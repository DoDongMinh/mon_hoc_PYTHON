import numpy as np

diem_list = [8.5, 7.0, 9.2, 6.5, 5.5]
diem_array = np.array(diem_list)
print(type(diem_list), type(diem_array))

diem_cong_them = diem_array + 0.5
print("Diem sau khi cong them 0.5:\n", diem_cong_them)

diem_cong_them_list = [diem + 0.5 for diem in diem_list]
print("Diem cong them bang list comprehension:\n", diem_cong_them_list)

print("Trung binh:", np.mean(diem_array))
print("Lon nhat:", np.max(diem_array))
print("Nho nhat:", np.min(diem_array))
print("Do lech chuan:", round(np.std(diem_array), 2))

ma_tran = np.array([[1, 2, 3], [4, 5, 6]])
print("Ma tran:\n", ma_tran)
print("Kich thuoc (shape):", ma_tran.shape)
print("Ma tran nhan 2:\n", ma_tran * 2)

#Yêu cầu: giải thích vì sao diem_array + 0.5 cộng được trực tiếp cho cả mảng, trong khi diem_list + 0.5 sẽ báo lỗi (gợi ý: toán tử + trên list
# thường dùng để nối 2 list, không phải cộng từng phần tử). 
'''
Trong Python, khi sử dụng toán tử `+` trên một danh sách (list), nó được hiểu là phép nối hai danh sách lại với nhau. Ví dụ, nếu bạn có một danh
sách `diem_list` và cố gắng thực hiện `diem_list + 0.5`, Python sẽ không biết cách xử lý vì `0.5` không phải là một danh sách, dẫn đến lỗi.
   
'''

