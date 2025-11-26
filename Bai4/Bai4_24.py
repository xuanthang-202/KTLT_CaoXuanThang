print("Sinh vien: Cao Xuan Thang")
print("Ma so SV: 245752021610145")
print("##########################")
################################
def dem_chu_hoa_va_chu_thuong():
    cau = input("Nhap mot cau: ")
    
    so_chu_hoa = 0
    so_chu_thuong = 0
    
    for ky_tu in cau:
        if ky_tu.isupper():
            so_chu_hoa += 1
        elif ky_tu.islower():
            so_chu_thuong += 1
            
    print("So chu hoa:", so_chu_hoa)
    print("So chu thuong:", so_chu_thuong)

dem_chu_hoa_va_chu_thuong()
