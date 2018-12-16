import math

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class triangle:
    def __init__(self, a, h, p):

# Функция для узнавания длины отрезка

        def side(point1, point2):
            return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

        self.a = a
        self.h = h
        self.p = p
        self.AH = side(self.a, self.h)
        self.HP = side(self.h, self.p)
        self.PA = side(self.p, self.a)

# Вычисляем площадь по формуле Герона

    def square(self):
        semi_perimetr = self.perimeter() / 2

        return round(math.sqrt(semi_perimetr
                         * (semi_perimetr - self.AH)
                         * (semi_perimetr - self.HP)
                         * (semi_perimetr - self.PA)))

# Вычисляем периметр

    def perimeter(self):
            return round(self.AH + self.HP + self.PA)

# Вычисляем высоту

    def height(self):
        return round(self.square() / (self.AH / 2))

# Проверка программы

# tt = triangle((4, 2), (1, 8), (12, 0))
#
# print("Площадь треугольника = {} см".format(tt.square()))
# print("Высота треугольника = {} см".format(tt.height()))
# print("Периметр треугольника = {} см".format(tt.perimeter()))

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

# Функция для узнавания длины отрезка

def side(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

class trapeze:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.AB = side(self.a, self.b)
        self.BC = side(self.b, self.c)
        self.CD = side(self.c, self.d)
        self.DA = side(self.d, self.a)
        self.diagonal_AC = side(self.a, self.c)
        self.diagonal_BD = side(self.b, self.d)

    def perimeter(self):
        return round(self.AB + self.BC + self.CD + self.DA)

# Представим площадь трапеции как два треугольника и сложим их

    def square(self):
        semi_perimeter1 = self.AB + self.diagonal_BD + self.DA / 2
        semi_perimeter2 = self.diagonal_BD + self.BC + self.CD / 2
        itog1 = math.sqrt(semi_perimeter1
                          * (semi_perimeter1 - self.AB)
                          * (semi_perimeter1 - self.diagonal_BD)
                          * (semi_perimeter1 - self.DA))

        itog2 = math.sqrt(semi_perimeter2
                          * (semi_perimeter2 - self.diagonal_BD)
                          * (semi_perimeter2 - self.BC)
                          * (semi_perimeter2 - self.CD))

        all_itog = itog1 + itog2
        return round(all_itog)

# Легче сделать функцию и все будет проще)

#     def fun_square(dot1, dot2, dot3):
#         semi_perimetr = (dot1 + dot2 + dot3) / 2
#         return math.sqrt(semi_perimetr
#                          * (semi_perimetr - dot1)
#                          * (semi_perimetr - dot2)
#                          * (semi_perimetr - dot3))

    def trapeze_test(self):
       if self.diagonal_AC == self.diagonal_BD:
           return True
       return False

# Проверка программы

# tt = trapeze((4, 2), (1, 8), (12, 0), (10, 2))
#
# print("Площадь равнобочной трапеции = {} см".format(tt.square()))
# print("Проверка на то что является ли фигура равнобочной трапецией = {}".format(tt.trapeze_test()))
# print("Периметр Площадь равнобочной трапеции = {} см".format(tt.perimeter()))