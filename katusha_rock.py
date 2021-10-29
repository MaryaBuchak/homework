import math
import matplotlib.pyplot as mpp

MODEL_DT = 0.001
MODEL_G = 9.81

class Rocket:
    def __init__(self, x, y, m, v_y, v_x, name):
        self.x = x
        self.y = y
        self.s_x = []
        self.s_y = []
        self.m_0 = m
        self.m = m
        self.v_x = v_x
        self.v_y = v_y
        self.name=name
    def up(self):

        self.s_x.append(self.x)
        self.s_y.append(self.y)
        self.x += self.v_x * MODEL_DT
        self.y += self.v_y * MODEL_DT
        self.m -= self.m_0*(1/2000)
        if self.m <= 0:
            self.padaem()

    def padaem(self):
        while self.y > 0:
            self.x += self.v_x * MODEL_DT
            self.v_y -= MODEL_G * MODEL_DT
            self.y += self.v_y * MODEL_DT
            if self.y < 0:
                self.y = 0
            self.s_y.append(self.y)
            self.s_x.append(self.x)


a = Rocket(100, 500, 15, 50, 50, "Катюша")
while a.m > 0:
    a.up()

mpp.plot(a.s_x, a.s_y)
mpp.show()
