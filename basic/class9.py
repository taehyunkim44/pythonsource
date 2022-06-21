# private : __변수명
# 자바와 마찬가지로 private를 쓰면 외부에서 가지고 올 수 없음 --> 자바처럼 getter , setter로 가져올 수 있음
import math


class Circle:
    def __init__(self, radius) -> None:
        self.__radius = radius

    def get_circumference(self):
        return 2 * math.pi * self.__radius

    def get_circle_area(self):
        return math.pi * (self.__radius**2)

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius


circle = Circle(10)
print("둘레", circle.get_circumference())
print("면적", circle.get_circle_area())
# print("__radius", circle.__radius) # 자바처럼 getter , setter로 가져올 수 있음
print("__radius", circle.get_radius())

print()
circle.set_radius(5)
print("둘레 ", circle.get_circumference())
print("면적 ", circle.get_circle_area())
