# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class Triangle:
    
    def __init__(self, ax, ay, bx, by, cx, cy):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy
        self.a_b = math.sqrt(((bx - ax)**2) + ((by - ay)**2))
        self.b_c = math.sqrt(((cx - bx)**2) + ((cy - by)**2))
        self.c_a = math.sqrt(((cx - ax)**2) + ((cy - ay)**2))

    def perimeter(self):
        self.perimeter = (self.a_b + self.b_c + self.c_a)
        return (self.perimeter)

    def area(self):
        self.semiperimeter = (self.a_b + self.b_c + self.c_a) / 2
        self.area = math.sqrt(self.semiperimeter * (self.semiperimeter - self.a_b) * (self.semiperimeter - self.b_c) * (self.semiperimeter - self.c_a))
        return (self.area)

    def height(self):
        self.height = (self.area * 2 / self.c_a)
        return (self.height)

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class IsoscelesTrapezoid:
    def __init__(self, ax, ay, bx, by, cx, cy, dx, dy):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy
        self.dx = dx
        self.dy = dy
        self.a_b = math.sqrt(((bx - ax)**2) + ((by - ay)**2))
        self.b_c = math.sqrt(((cx - bx)**2) + ((cy - by)**2))
        self.c_d = math.sqrt(((cx - dx)**2) + ((cy - dy)**2))
        self.d_a = math.sqrt(((ax - dx)**2) + ((ay - dy)**2))
        self.a_c = math.sqrt(((cx - ax)**2) + ((cy - ay)**2))
        self.b_d = math.sqrt(((dx - bx)**2) + ((dy - by)**2))

    def is_isosceles_trapezoid(self):
        return self.a_c == self.b_d

    def perimeter(self):
        self.perimeter = (self.a_b + self.b_c + self.c_d + self.d_a)
        return (self.perimeter)

    def area(self):
        self.area = ((self.b_c + self.d_a) / 2) * math.sqrt(self.a_b ** 2 - ((self.d_a - self.b_c) ** 2 / 4))
        return (self.area)
