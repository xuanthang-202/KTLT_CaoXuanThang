print("Sinh vien: Cao Xuan Thang")
print("Ma so SV : 245752021610145")
print("###########################")
#################################
ds = input('Danh sach cac tu: ').split() 

tu_dai_nhat = ds[0] 

for tu in ds[1:]:
    if len(tu) > len(tu_dai_nhat):
        tu_dai_nhat = tu

print(f"Tu dai nhat la: {tu_dai_nhat}")
