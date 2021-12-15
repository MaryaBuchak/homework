import random

class ring_18:
     def sum(self, d, o):
         return (d + o) % 18

     def multiply(self, g, o):
         return (g * o) % 18

love = ring_18()
d = random.randint(0, 19)
o = random.randint(0, 19)
g = random.randint(0, 19)

print(d, o, g)

print("Ассоциативность сложения")
h = love.sum(d, love.sum(o, g))
print(h)
p = love.sum(love.sum(d, o), g)
print(p)
print(h == p)

print("Нейтральный элемент по сложению")
h = love.sum(0, d)
print(h)
p = love.sum(d, 0)
print(p)
print(h == p)

print("Обратимость сложения")
h = love.sum(d, -d)
print(h)
p = love.sum(-d, d)
print(p)
print(h == p)

print("Коммутативность сложения")
h = love.sum(d, o)
print(h)
p = love.sum(o, d)
print(p)
print(h == p)

print("Ассоциативность умножения")
h = love.multiply(d, love.multiply(o, g))
print(h)
p = love.multiply(love.multiply(d, o), g)
print(p)
print(h == p)

print("Нейтральный элемент по умножению")
h = love.multiply(1, d)
print(h)
p = love.multiply(d, 1)
print(p)
print(h == p)

print("Коммутативность умножению")
h = love.multiply(d, o)
print(h)
p = love.multiply(o, d)
print(p)
print(h == p)

print("Диструбитовность")
h = love.multiply(d, love.sum(o, g))
print(h)
p = love.sum(love.sum(d, o), love.sum(d, g))
print(p)
print(h == p)

print("Коммутативное колько с единицой Z/18Z\n")