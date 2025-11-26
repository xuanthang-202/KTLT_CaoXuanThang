print("Sinh vien: Cao Xuan Thang")
print("Ma so SV: 245752021610145")
print("##########################")
################################
def dem_chu_cai_va_chu_so():
    cau = input("Nhap mot cau: ")
    
    so_chu_cai = 0
    so_chu_so = 0
    
    for ky_tu in cau:
        if ky_tu.isalpha():
            so_chu_cai += 1
        elif ky_tu.isdigit():
            so_chu_so += 1
            
    print("So chu cai:", so_chu_cai)
    print("So chu so:", so_chu_so)

dem_chu_cai_va_chu_so()
