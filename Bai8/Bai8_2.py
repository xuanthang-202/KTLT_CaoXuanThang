print("Sinh vien: Cao Xuan Thang")
print("Ma so SV : 245752021610145")
print("###########################")
#################################
import turtle
import random
# Danh sách các màu sẽ được chọn ngẫu nhiên
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]
# Thiết lập màn hình đồ họa
window = turtle.Screen()
window.bgcolor("white") # Đặt màu nền trắng
# Thiết lập đối tượng rùa (bút vẽ)
painter = turtle.Turtle()
painter.pensize(3)
painter.speed(0) # Tốc độ vẽ nhanh nhất
# Vòng lặp chính để vẽ 10 hình tròn
for i in range(10):
    # 1. Chọn màu ngẫu nhiên từ danh sách
    color = random.choice(colors)
    painter.pencolor(color)
    # 2. Vẽ hình tròn bán kính 100
    painter.circle(100)    
    # 3. Thay đổi hướng
    painter.right(30) # Xoay phải 30 độ
    painter.left(60)  # Xoay trái 60 độ (tổng cộng rùa xoay trái 30 độ so với hướng ban đầu)    
    # 4. Di chuyển rùa về vị trí bắt đầu 
    painter.setposition(0, 0) 
window.mainloop() # Giữ cửa sổ đồ họa mở
