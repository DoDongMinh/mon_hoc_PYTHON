import requests

# Bài tập 5.1
print("--- API Github ---")
response_github = requests.get("https://api.github.com/repos/python/cpython")
if response_github.status_code == 200:
    du_lieu = response_github.json()
    print("Ten repository:", du_lieu["full_name"])
    print("So luot gan sao (stars):", du_lieu["stargazers_count"])
    print("Ngon ngu chinh:", du_lieu["language"])
else:
    print("Goi API that bai, ma loi:", response_github.status_code)

#Bài tập 5.2
print("\n--- API Ty gia ---")
response_tygia = requests.get("https://open.er-api.com/v6/latest/USD")
if response_tygia.status_code == 200:
    du_lieu_tygia = response_tygia.json()
    ty_gia_vnd = du_lieu_tygia["rates"]["VND"]
    print(f"1 USD = {ty_gia_vnd:,.0f} VND")
else:
    print("Khong lay duoc ty gia, ma loi:", response_tygia.status_code)