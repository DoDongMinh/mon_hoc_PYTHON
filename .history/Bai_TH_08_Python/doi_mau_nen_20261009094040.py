# Bài tập 4.1
'''
import tkinter as tk 
danh_sach_mau = ["white", "lightblue", "lightgreen", "lightyellow", "lightpink"] 
vi_tri_mau_hien_tai = 0 
def doi_mau_nen():



 global vi_tri_mau_hien_tai 
 vi_tri_mau_hien_tai = (vi_tri_mau_hien_tai + 1) % len(danh_sach_mau)  
 cua_so.configure(bg=danh_sach_mau[vi_tri_mau_hien_tai]) 
cua_so = tk.Tk() 
cua_so.title("Doi mau nen") 
cua_so.geometry("350x200") 
nut_doi_mau = tk.Button(cua_so, text="Doi mau nen", command=doi_mau_nen) 
nut_doi_mau.pack(pady=80) 
cua_so.mainloop()

'''
# Bài tập 4.2 
import tkinter as tk 
so_lan_bam = 0 
def tang_so_lan_bam(): 
 global so_lan_bam 
 so_lan_bam += 1 
 nhan_dem.config(text=f"So lan da bam: {so_lan_bam}") 
cua_so = tk.Tk() 
cua_so.title("Dem so lan bam nut") 
cua_so.geometry("350x200") 
nhan_dem = tk.Label(cua_so, text="So lan da bam: 0", font=("Arial", 14)) 
nhan_dem.pack(pady=20) 
nut_bam = tk.Button(cua_so, text="Bam vao day", command=tang_so_lan_bam) 
nut_bam.pack(pady=10) 
cua_so.mainloop()

