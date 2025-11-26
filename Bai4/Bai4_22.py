print("Sinh vien: Cao Xuan Thang")
print("Ma so SV : 245752021610145")
print("###########################")
#################################
def kiem_tra_tat_ca_chu_so_chan(so):
    chuoi_so = str(so)
    
    for chu_so in chuoi_so:
        gia_tri = int(chu_so)
        
        if gia_tri % 2 != 0:
            return False
            
    return True

ds_ket_qua = []

for so in range(1000, 3001):
    if kiem_tra_tat_ca_chu_so_chan(so):
        ds_ket_qua.append(str(so))

print(",".join(ds_ket_qua))
