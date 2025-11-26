print("Sinh vien: Cao Xuan Thang")
print("Ma so SV : 245752021610145")
print("###########################")
#################################
import turtle
# Thiết lập màn hình đồ họa
window = turtle.Screen()
window.bgcolor("lightblue") # Đổi màu nền thành "lightblue" để dễ nhìn hơn
# Thiết lập đối tượng rùa (bút vẽ)
painter = turtle.Turtle()
painter.color('red', 'yellow') # Đặt màu bút là đỏ, màu tô là vàng
painter.pensize(2)
# Hàm vẽ hình vuông
def drawsq(t, s):
    """Vẽ một hình vuông với cạnh dài s sử dụng rùa t."""
    t.begin_fill()
    for _ in range(4):
        t.forward(s)
        t.left(90)
    t.end_fill()
# Thiết lập ban đầu cho rùa
painter.speed(0) # Tốc độ vẽ nhanh nhất
# Vòng lặp chính để vẽ hình
for i in range(18): # Giảm số lần lặp để hình dễ quan sát và tính toán hơn
    painter.left(20) # Xoay 20 độ (360 / 18 = 20)
    drawsq(painter, 100) # Vẽ hình vuông cạnh 100
window.mainloop() # Giữ cửa sổ đồ họa mở
