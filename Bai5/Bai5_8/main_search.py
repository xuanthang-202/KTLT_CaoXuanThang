print("Sinh vien: Cao Xuan Thang")
print("Ma so SV : 245752021610145")
print("###########################")
#################################
import search_module
def get_list_and_item():
    """Nhận danh sách phần tử và giá trị cần tìm từ người dùng."""    
    # 1. Nhập danh sách
    data_input = input("Nhập các phần tử của danh sách, cách nhau bằng dấu phẩy: ")
    try:
        # Chuyển đổi các chuỗi nhập vào thành số nguyên (có thể dùng float nếu cần)
        dlist = [int(x.strip()) for x in data_input.split(',')]
    except ValueError:
        print("Lỗi: Vui lòng đảm bảo tất cả phần tử là số nguyên.")
        return None, None
    # 2. Nhập giá trị cần tìm
    while True:
        try:
            item = int(input("Nhập giá trị cần tìm (item): "))
            break
        except ValueError:
            print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")            
    return dlist, item
# --- Chương trình chính ---
dlist, item = get_list_and_item()
if dlist is not None and item is not None:
    # Sử dụng hàm tìm kiếm từ module
    found_status, position = search_module.Sequential_Search(dlist, item)
    print("\n--- Kết quả Tìm kiếm ---")
    print(f"Danh sách: {dlist}")
    print(f"Giá trị cần tìm: {item}")    
    if found_status:
        print(f"Sequential_Search -> (True, {position})")
        print(f"Kết quả: Phần tử được tìm thấy tại chỉ mục (Index) {position}.")
    else:
        print(f"Sequential_Search -> (False, {position})")
        print(f"Kết quả: Phần tử không được tìm thấy.")
