import random


class Ring18:
    def __init__(self, v):
        self.v = v % 18

    def __str__(self):
        return '{}'.format(self.v)

    def __add__(self, other):
        return Ring18(self.v + other.v)

    def __sub__(self, other):
        return Ring18(self.v - other.v)

    def __mul__(self, other):
        return Ring18(self.v * other.v)

    def __eq__(self, other):
        return self.v == other.v


d = Ring18(random.randint(-1000, 1000))
o = Ring18(random.randint(-1000, 1000))
g = Ring18(random.randint(-1000, 1000))

print(d, o, g)

print("Ассоциативность сложения")
h = d + (o + g)
print(h)
p = (d + o) + g
print(p)
print(h == p)

print("Нейтральный элемент по сложению")
h = Ring18(0) + d
print(h)
p = d + Ring18(0)
print(p)
print(h == p)

print("Обратимость сложения")
h = d - d
print(h)
p = d - d
print(p)
print(h == p)

print("Коммутативность сложения")
h = d + o
print(h)
p = o + d
print(p)
print(h == p)

print("Ассоциативность умножения")
h = d * (o + g)
print(h)
p = (d * o) * g
print(p)
print(h == p)

print("Нейтральный элемент по умножению")
h = Ring18(1) * d
print(h)
p = d * Ring18(1)
print(p)
print(h == p)

print("Коммутативность умножению")
h = d * o
print(h)
p = o * d
print(p)
print(h == p)

print("Дистрибутивность")
h = d * (o + g)
print(h)
p = (d * o) + (d * g)
print(p)
print(h == p)

print("Коммутативное колько с единицой Z/18Z\n")
