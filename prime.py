import random

def prime(n):
    a = random.randint(2, n - 1)
    if a**(n-1) % n == 1:
        return True
    else:
        return False

print("Введите число (пожалуйста, не число Кармайкла): ")
a = int(input())
print(prime(a))