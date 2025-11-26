print("Sinh vien: Cao Xuan Thang")
print("Ma so SV : 245752021610145")
print("###########################")
#################################
def kiem_tra_chia_het_cho_5():
    
    chuoi_nhap = input("Nhap chuoi so nhi phan 4 chu so (cach nhau boi dau phay): ")
    ds_nhi_phan = chuoi_nhap.split(',')
    
    ds_chia_het = []
    
    for so_nhi_phan in ds_nhi_phan:
        so_nhi_phan_cat = so_nhi_phan.strip()
        
        if len(so_nhi_phan_cat) != 4 or not all(c in '01' for c in so_nhi_phan_cat):
            continue

        gia_tri_thap_phan = int(so_nhi_phan_cat, 2)
        
        if gia_tri_thap_phan % 5 == 0:
            ds_chia_het.append(so_nhi_phan_cat)
            
    print("Dau ra se la:")
    print(",".join(ds_chia_het))

kiem_tra_chia_het_cho_5()
