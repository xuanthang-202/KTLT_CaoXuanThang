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
        # Chuyển đổi các chuỗi nhập vào thành số nguyên
        dlist = [int(x.strip()) for x in data_input.split(',')]
    except ValueError:
        print("Lỗi: Vui lòng đảm bảo tất cả phần tử là số nguyên.")
        return None, None
    # 2. Nhập giá trị cần tìm
    while True:
        try:
            item = int(input("Nhập giá trị cần tìm (value): "))
            break
        except ValueError:
            print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")            
    return dlist, item
# --- Chương trình chính ---
dlist_raw, item = get_list_and_item()
if dlist_raw is not None and item is not None:    
    # 3. Quan trọng: Sắp xếp danh sách trước khi tìm kiếm nhị phân
    dlist_sorted = sorted(dlist_raw)    
    # 4. Sử dụng hàm tìm kiếm nhị phân từ module
    found_status, position = search_module.binary_search(dlist_sorted, item)
    print("\n--- Kết quả Tìm kiếm Nhị phân ---")
    print(f"Danh sách ban đầu: {dlist_raw}")
    print(f"Danh sách đã sắp xếp: {dlist_sorted}")
    print(f"Giá trị cần tìm: {item}")    
    if found_status:
        print(f"binary_search -> (True, {item})")
        print(f"Kết quả: Phần tử được tìm thấy tại chỉ mục (Index) {position} trong danh sách đã sắp xếp.")
    else:
        print(f"binary_search -> (False, {item})")
        print(f"Kết quả: Phần tử không được tìm thấy.")
