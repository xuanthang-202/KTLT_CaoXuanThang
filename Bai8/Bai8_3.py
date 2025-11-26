print("Sinh vien: Cao Xuan Thang")
print("Ma so SV : 245752021610145")
print("###########################")
#################################
import turtle
# Thiết lập màn hình đồ họa
window = turtle.Screen()
window.bgcolor("white")
window.title("Hoa Văn Hình Tròn")
# Thiết lập đối tượng rùa (bút vẽ)
painter = turtle.Turtle()
painter.pensize(2)
painter.speed(0) # Tốc độ vẽ nhanh nhất
# Danh sách 3 màu cần dùng
colors = ["red", "green", "blue"] 
# Góc xoay cho mỗi hình tròn
angle_per_circle = 360 / 18 # Ta sẽ vẽ 18 hình tròn (6 hình x 3 màu)
# Vòng lặp chính để vẽ hoa văn
# Ta sẽ lặp 18 lần để đảm bảo hoa văn đóng kín (18 * 20 = 360)
for i in range(18):
    # Chọn màu dựa trên chỉ số i để lặp lại 3 màu:
    # 0%3=0 (red), 1%3=1 (green), 2%3=2 (blue), 3%3=0 (red),...
    current_color = colors[i % 3]
    painter.pencolor(current_color)    
    # 1. Vẽ hình tròn bán kính 80 (hoặc kích thước phù hợp)
    painter.circle(80)    
    # 2. Xoay rùa để chuẩn bị vẽ hình tròn tiếp theo
    painter.left(angle_per_circle) 
window.mainloop()
