print("Sinh vien: Cao Xuan Thang")
print("Ma so SV : 245752021610145")
print("###########################")
#################################
import sort_module
def get_list_from_user():
    """Nhận danh sách phần tử từ người dùng."""    
    data_input = input("Nhập các phần tử của danh sách, cách nhau bằng dấu phẩy: ")
    try:
        # Chuyển đổi các chuỗi nhập vào thành số nguyên
        # Sử dụng .strip() để loại bỏ khoảng trắng thừa
        nlist = [int(x.strip()) for x in data_input.split(',')]
        return nlist
    except ValueError:
        print("Lỗi: Vui lòng đảm bảo tất cả phần tử là số nguyên và nhập đúng định dạng.")
        return None
# --- Chương trình chính ---
nlist = get_list_from_user()
if nlist is not None:
    # Sao chép danh sách để giữ lại bản gốc (nếu cần) và truyền bản sao vào hàm
    list_to_sort = nlist[:]     
    print("\n--- Kết quả Sắp xếp Nổi bọt ---")
    print(f"Danh sách ban đầu: {list_to_sort}")    
    # Sử dụng hàm sắp xếp từ module
    sorted_list = sort_module.bubbleSort(list_to_sort)
    print(f"Danh sách đã sắp xếp: {sorted_list}")
