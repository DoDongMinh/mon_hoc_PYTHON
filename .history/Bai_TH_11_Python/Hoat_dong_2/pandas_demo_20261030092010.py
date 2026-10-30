import pandas as pd

# Bài tập 2.1
df = pd.read_csv("diem_sinh_vien.csv")
print("--- 5 dong dau ---")
print(df.head())
print("Kich thuoc:", df.shape)
print("Danh sach cot:", df.columns.tolist())

# Bài tập 2.2
print("\n--- Thong ke theo mon hoc ---")
diem_trung_binh_mon = df.groupby("mon_hoc")["diem"].mean()
print(diem_trung_binh_mon)
print("Diem trung binh toan bo:", df["diem"].mean())
print("Diem cao nhat:", df["diem"].max())
print("Diem thap nhat:", df["diem"].min())

# Bài tập 2.3
print("\n--- DTB sinh vien & Loc dat/khong dat ---")
diem_tb_sv = df.groupby("ho_ten")["diem"].mean().round(2)
print(diem_tb_sv)
sinh_vien_dat = diem_tb_sv[diem_tb_sv >= 5.0]
sinh_vien_khong_dat = diem_tb_sv[diem_tb_sv < 5.0]

print("\nSinh vien dat:")
print(sinh_vien_dat)
print("\nSinh vien khong dat:")
print(sinh_vien_khong_dat)