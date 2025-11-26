print("Sinh vien: Cao Xuan Thang")
print("Ma so SV : 245752021610145")
print("###########################")
#################################
import math
class Circle(object):
    """Class đại diện cho hình tròn và tính toán các thuộc tính của nó."""
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        """Tính diện tích hình tròn (Pi * r^2)."""
        return math.pi * (self.radius ** 2)
    def perimeter(self):
        """Tính chu vi hình tròn (2 * Pi * r)."""
        return 2 * math.pi * self.radius
# Tạo đối tượng
my_circle = Circle(5) # Bán kính r = 5
print('--- Kết quả Hình tròn ---')
print('Bán kính:', my_circle.radius)
print('Diện tích:', my_circle.area())
print('Chu vi:', my_circle.perimeter())
