danh_sach_sach = [
    {
        "ma_sach": "S001",
        "ten_sach": "Lap trinh Python",
        "tac_gia": "Nguyen Van An",
        "nam_xuat_ban": 2024,
        "trang_thai": "Con"
    },
    {
        "ma_sach": "S002",
        "ten_sach": "Co so du lieu",
        "tac_gia": "Tran Thi Binh",
        "nam_xuat_ban": 2023,
        "trang_thai": "Con"
    },
    {
        "ma_sach": "S003",
        "ten_sach": "Lap trinh Web",
        "tac_gia": "Le Van Cuong",
        "nam_xuat_ban": 2022,
        "trang_thai": "Con"
    }
]

lich_su_muon = []


def hien_thi_danh_sach_sach():
    if len(danh_sach_sach) == 0:
        print("-> Thu vien chua co sach.")
        return

    print("\n" + "=" * 90)
    print(f"{'Ma sach':<10}{'Ten sach':<25}{'Tac gia':<22}"
          f"{'Nam XB':<10}{'Trang thai':<12}")
    print("-" * 90)

    for sach in danh_sach_sach:
        print(f"{sach['ma_sach']:<10}{sach['ten_sach']:<25}"
              f"{sach['tac_gia']:<22}{sach['nam_xuat_ban']:<10}"
              f"{sach['trang_thai']:<12}")

    print("=" * 90)


def tim_sach_theo_ma(ma_sach):
    for sach in danh_sach_sach:
        if sach["ma_sach"] == ma_sach:
            return sach
    return None


def xem_sach_con():
    sach_con = [sach for sach in danh_sach_sach
                if sach["trang_thai"] == "Con"]

    if len(sach_con) == 0:
        print("-> Hien khong con sach nao dang co trong thu vien.")
        return

    print("\nCAC SACH DANG CON:")
    for sach in sach_con:
        print(f" {sach['ma_sach']} - {sach['ten_sach']} "
              f"- {sach['tac_gia']} - {sach['nam_xuat_ban']}")


def them_sach(ma_sach, ten_sach, tac_gia, nam_xuat_ban):
    if tim_sach_theo_ma(ma_sach) is not None:
        print(f"-> Ma sach {ma_sach} da ton tai, khong the them.")
        return

    danh_sach_sach.append({
        "ma_sach": ma_sach,
        "ten_sach": ten_sach,
        "tac_gia": tac_gia,
        "nam_xuat_ban": nam_xuat_ban,
        "trang_thai": "Con"
    })

    print(f"-> Da them sach {ma_sach} thanh cong.")


def muon_sach(ma_sach, ten_nguoi_muon):
    sach = tim_sach_theo_ma(ma_sach)

    if sach is None:
        print(f"-> Khong tim thay sach {ma_sach}.")
        return

    if sach["trang_thai"] == "Dang muon":
        print(f"-> Sach {ma_sach} dang duoc muon, khong the muon tiep.")
        return

    sach["trang_thai"] = "Dang muon"

    lich_su_muon.append({
        "ma_sach": ma_sach,
        "ten_sach": sach["ten_sach"],
        "ten_nguoi_muon": ten_nguoi_muon,
        "trang_thai": "Dang muon"
    })

    print(f"-> Muon sach {ma_sach} cho {ten_nguoi_muon} thanh cong.")


def tra_sach(ma_sach):
    sach = tim_sach_theo_ma(ma_sach)

    if sach is None:
        print(f"-> Khong tim thay sach {ma_sach}.")
        return

    if sach["trang_thai"] == "Con":
        print(f"-> Sach {ma_sach} dang o thu vien, khong can tra.")
        return

    sach["trang_thai"] = "Con"

    for gd in lich_su_muon:
        if gd["ma_sach"] == ma_sach and gd["trang_thai"] == "Dang muon":
            gd["trang_thai"] = "Da tra"
            break

    print(f"-> Tra sach {ma_sach} thanh cong.")


def thong_ke_muon():
    if len(lich_su_muon) == 0:
        print("-> Chua co giao dich muon sach nao.")
        return

    print("\nLICH SU MUON SACH:")
    so_luot = 0

    for gd in lich_su_muon:
        print(f" {gd['ma_sach']} - {gd['ten_sach']} - "
              f"{gd['ten_nguoi_muon']} - {gd['trang_thai']}")
        so_luot += 1

    print(f"\n>>> TONG SO LUOT MUON: {so_luot}")


def nhap_so_nguyen(loi_nhac):
    while True:
        try:
            return int(input(loi_nhac))
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap lai mot so nguyen.")


def hien_thi_menu():
    print("\n===== QUAN LY THU VIEN =====")
    print("1. Hien thi danh sach tat ca sach")
    print("2. Xem cac sach dang con")
    print("3. Them sach moi")
    print("4. Muon sach")
    print("5. Tra sach")
    print("6. Thong ke lich su muon")
    print("0. Thoat chuong trinh")


def chay_chuong_trinh():
    while True:
        hien_thi_menu()
        lua_chon = input("Nhap lua chon cua ban: ").strip()

        if lua_chon == "1":
            hien_thi_danh_sach_sach()

        elif lua_chon == "2":
            xem_sach_con()

        elif lua_chon == "3":
            ma_sach = input("Nhap ma sach moi: ").strip().upper()
            ten_sach = input("Nhap ten sach: ").strip().title()
            tac_gia = input("Nhap ten tac gia: ").strip().title()
            nam_xuat_ban = nhap_so_nguyen("Nhap nam xuat ban: ")

            them_sach(ma_sach, ten_sach, tac_gia, nam_xuat_ban)

        elif lua_chon == "4":
            ma_sach = input("Nhap ma sach can muon: ").strip().upper()
            ten_nguoi_muon = input("Nhap ten nguoi muon: ").strip().title()

            muon_sach(ma_sach, ten_nguoi_muon)

        elif lua_chon == "5":
            ma_sach = input("Nhap ma sach can tra: ").strip().upper()

            tra_sach(ma_sach)

        elif lua_chon == "6":
            thong_ke_muon()

        elif lua_chon == "0":
            print("Cam on da su dung chuong trinh. Tam biet!")
            break

        else:
            print("-> Lua chon khong hop le, vui long chon lai.")


if __name__ == "__main__":
    chay_chuong_trinh()
