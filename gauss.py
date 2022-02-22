from numpy.linalg import norm
from numpy.linalg import solve as solve_out_of_the_box
import numpy



def gauss(a, b):
    a = a.copy()
    b = b.copy()

    def forward():
        # do something to a and b

        for k in range(len(a) - 1):
            for i in range(k + 1, len(a)):
                poleno = -(a[i, k] / a[k, k])
                for j in range(len(a) + 1):
                    if j < len(a):
                        a[i, j] += poleno * a[k, j]
                    else:
                        b[j - len(a) + i] += poleno * b[k]
    #                 Я очень сильно люблю сериал "Счастливы вместе", Дмитрий Вадимович



    def backward():
        x = numpy.zeros(len(b), dtype=float)
        # then do something to a and b

        for i in range(len(a) - 1, -1, -1):
            if i == len(a) - 1:
                x[i] = b[i] / a[i, i]
            else:
                p = 0
                for j in range(i + 1, len(a)):
                    p += a[i, j] * x[j]
                x[i] = (b[i] - p) / a[i, i]

        return x

    forward()
    x = backward()
    return x

a = numpy.array([
    [1.5, 2.0, 1.5, 2.0],
    [3.0, 2.0, 4.0, 1.0],
    [1.0, 6.0, 0.0, 4  ],
    [2.0, 1.0, 4.0, 3  ]
], dtype=float)

b = numpy.array([5, 6, 7, 8], dtype=float)

oob_solution = solve_out_of_the_box(a, b)
solution = gauss(a, b)

print(solution)
print("Макс отклонение компоненты решения:", norm(solution-oob_solution, ord=1))