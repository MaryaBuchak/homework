import math
import matplotlib.pyplot as mpp

MODEL_G = 9.81
MODEL_DT = 0.001

class Body:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        self.trajektory_x = []
        self.trajektory_y = []

    def advance(self):
        self.trajektory_x.append(self.x)
        self.trajektory_y.append(self.y)

        self.x += self.vx * MODEL_DT
        self.y += self.vy * MODEL_DT
        self.vy -= MODEL_G * MODEL_DT


class Rocket(Body):
    def __init__(self, x, y, vx, vy, a, name, m, vm):
        super().__init__(x, y, vx, vy)
        self.a = a
        self.m = m
        self.vm = vm
        self.name = name

    def advance(self):
        super().advance()
        if self.m > 0:
            if self.m - self.vm * MODEL_DT > 0:
                self.m -= self.vm * MODEL_DT
            else:
                self.m = 0
            self.vy += self.a * MODEL_DT


katya = Rocket(0, 0, 5, 5, 10, 'Katya', 100, 100)
stone = Body(100, 100, 10, 10)
time = 0

while time < 2:
    katya.advance()
    stone.advance()
    time += MODEL_DT

mpp.plot(katya.trajektory_x, katya.trajektory_y)
mpp.show()

mpp.plot(stone.trajektory_x, stone.trajektory_y)
mpp.show()