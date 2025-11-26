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
    print("Vui lòng nhập các giá trị (chỉ số nguyên hoặc số thực):")
    for i in range(count):
        while True:
            try:
                # Nhận giá trị, chuyển thành số thực
                value = float(input(f"Nhập phần tử thứ {i + 1}: "))
                my_list.append(value)
                break
            except ValueError:
                print("Giá trị không hợp lệ. Vui lòng nhập một số.")
    
    return my_list

# 1. Nhập danh sách
data_list = get_list_from_user()

# 2. Sử dụng module để tìm Min và Max
min_val, max_val = list_ops.find_min_max(data_list)

# 3. Sử dụng module để tìm Vị trí (Index) của Min và Max
min_index, max_index = list_ops.find_min_max_index(data_list, min_val, max_val)

# 4. Sử dụng module để sắp xếp
sorted_list = list_ops.sort_list_asc(data_list)

print("\n--- Kết quả Phân tích ---")
print(f"Danh sách đã nhập: {data_list}")

if min_val is not None:
    print(f"Phần tử nhỏ nhất: {min_val} (Vị trí/Index: {min_index})")
    print(f"Phần tử lớn nhất: {max_val} (Vị trí/Index: {max_index})")
    
print(f"Danh sách sau khi sắp xếp (tăng dần): {sorted_list}")
