# Problem 6: Polymorphism (Shape)

# Shape base class এ area(self) method NotImplementedError("Subclass must implement area()") raise করবে।
# Rectangle(width, height) এবং Circle(radius) দুটি subclass বানাও, দুটোতেই area() override করো (math.pi ব্যবহার করবে)।
# print_area(shape) নামে standalone function লেখো যা "Area: <মান>" print করবে (২ দশমিক পর্যন্ত)।
# একটি list এ Rectangle(4, 5) ও Circle(3) রেখে loop চালিয়ে print_area call করো।
import math
class Shape:
    def area(self):
        raise NotImplementedError ("Subclass must implement area()")


class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return self.width*self.height

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return math.pi*self.radius**2

def print_area(Shape):
    print(f"Area: {Shape.area():.2f}")


for s in [Rectangle(4,5),Circle(3)]:
    print_area(s)