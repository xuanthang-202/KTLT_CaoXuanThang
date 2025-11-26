print("Sinh vien: Cao Xuan Thang")
print("Ma so SV: 245752021610145")
print("##########################")
################################
def tinh_so_tien_thuc():
    so_du = 0  # Khoi tao so du ban dau
    print("Nhap nhat ky giao dich (GUI tien: D <so_tien>, Rut tien: W <so_tien>). Nhap 'ket thuc' de tinh.")
    
    while True:
        giao_dich = input("> ").strip()
        
        if giao_dich.lower() == 'ket thuc':
            break
            
        # Tach lenh va gia tri
        phan_tu = giao_dich.split()
        if len(phan_tu) != 2:
            continue
            
        loai_giao_dich = phan_tu[0].upper()
        
        try:
            so_tien = int(phan_tu[1])
        except ValueError:
            print("So tien khong hop le.")
            continue
            
        if loai_giao_dich == 'D': # Deposit (Gửi tiền)
            so_du += so_tien
        elif loai_giao_dich == 'W': # Withdraw (Rút tiền)
            so_du -= so_tien
            
    print(f"\nSo tien thuc te cua tai khoan la: {so_du}")

tinh_so_tien_thuc()
