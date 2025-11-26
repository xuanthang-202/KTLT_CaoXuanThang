print("Sinh vien: Cao Xuan Thang")
print("Ma so SV: 245752021610145")
print("##########################")
################################
def loc_so_le():
    chuoi_so = input("Nhap cac so, cach nhau boi dau cach: ")
    ds_chuoi_so = chuoi_so.split()
    
    ds_so_le = []
    
    for chuoi_so_hien_tai in ds_chuoi_so:
        try:
            so = int(chuoi_so_hien_tai)
            # Kiem tra neu la so le (so du khac 0 khi chia cho 2)
            if so % 2 != 0:
                ds_so_le.append(so)
        except ValueError:
            # Bo qua neu co ki tu khong phai so
            continue
            
    print("Danh sach cac so le da loc:", ds_so_le)

loc_so_le()
