print("Sinh vien: Cao Xuan Thang")
print("Ma so SV : 245752021610145")
print("###########################")
#################################
import list_ops
def get_list_from_user():
    """Nhận số lượng và giá trị của danh sách từ bàn phím."""
    while True:
        try:
            count = int(input("Nhập số lượng phần tử của danh sách: "))
            if count <= 0:
                print("Số lượng phải lớn hơn 0. Vui lòng thử lại.")
                continue
            break
        except ValueError:
            print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")
    my_list = []
    print("Vui lòng nhập các giá trị:")
    for i in range(count):
        while True:
            try:
                value = float(input(f"Nhập phần tử thứ {i + 1}: "))
                my_list.append(value)
                break
            except ValueError:
                print("Giá trị không hợp lệ. Vui lòng nhập một số.")    
    return my_list
# 1. Nhập danh sách
data_list = get_list_from_user()
# 2. Tìm Min và Max (giá trị)
min_val, max_val = list_ops.find_min_max(data_list)
# 3. Tìm Vị trí (Index) của Min và Max
min_index, max_index = list_ops.find_min_max_index(data_list, min_val, max_val)
print("\n--- Vị trí (Index) kết quả ---")
print(f"Danh sách đã nhập: {data_list}")
if min_index is not None:
    print(f"Vị trí (Index) phần tử nhỏ nhất ({min_val}): {min_index}")
    print(f"Vị trí (Index) phần tử lớn nhất ({max_val}): {max_index}")
