import turtle as tl

def draw_fractal(scale):
    if scale >= 5:
        tl.pensize(2)
        draw_fractal(scale / 3)
        tl.left(45)
        draw_fractal(scale / 3)
        tl.right(90)
        draw_fractal(scale / 3)
        tl.left(45)
        tl.pensize(4)
        draw_fractal(scale / 3)
        tl.forward(30)
        draw_fractal(scale / 3)
        tl.right(30)
        draw_fractal(scale / 3)
        tl.backward(30)
        draw_fractal(scale / 6)

    else:
        tl.forward(scale)

scale =400
tl.penup()
tl.goto(-scale, -scale/2)
tl.pendown()

draw_fractal(scale)
tl.done()
