import random

def ferma(n):
    for i in range(25):
        if pow(random.randint(2, n - 1), n-1, n) != 1:
            return False
    return True

print("Введите число: ")
a = int(input())
print(ferma(a), '\n')
