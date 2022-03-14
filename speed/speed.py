#Эта программа позволяет понять, как иногда можно ускорять свой код.
# Данный пример ускорил вычисление числа пи в 11 раз.

import time
from numba import njit

@njit
def turtle(n):
    result = 0
    for i in range(n):
        result += (-1) ** i * 4 / (1 + 2 * i)
    return result

beggin_time = time.time()
print('Pi =', turtle(1000000000))
print('timework =', time.time()-beggin_time)
