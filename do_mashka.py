# Выгруз модуля, который предоставляет возможность воспользоватся тригонометрическими и логарифмическими функциями
import math
# Этот модуль предоставляет базовые методы для манипуляции с большими массивами и матрицами.
# Используется для того, чтобы получить аргумент (в данной программе) от 1 до 199.9
import numpy
# Модуль предоставляет возможность стоить графики. С помощью as мы перемеиновали модуль, чтобы к нему было легче обращаться
import matplotlib.pyplot as mpp

# Эта программа рисует график функции, заданной выражением ниже

# Проверяем, что программа запущенна, а не подключена, как библиотека 
if  __name__=='__main__':
# Получаем те самые значения аргумента от 0 до 199.9 включительно с шагом 0.1
    arguments = numpy.arange(0, 200, 0.1)

    # mpp.plot - рисует график функции, написанной ниже
    mpp.plot(
        arguments,
        [math.sin(a) * math.cos(a/20) for a in arguments]
        )
    # mpp.show - показывает нарисованный график функций 
    mpp.show()