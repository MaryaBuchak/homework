def eucklid(a, b):
    while a > 0 and b > 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b

print("Введите а и b: ")
a = int(input())
b = int(input())
print(eucklid(a, b))