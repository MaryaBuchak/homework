from turtle import turtle
from turtle_numba import turtle as turtle_numba
import time

n = 10_000_000

beggin_time = time.time()
print('Pi =', turtle(n))
timework1 = time.time()-beggin_time
print('Timework without numba =', timework1)

beggin_time = time.time()
print('Pi =', turtle_numba(n))
timework2 = time.time()-beggin_time
print('Timework with numba =', timework2)
print("Acceleration by " + str(int(timework1 // timework2)) + " times")