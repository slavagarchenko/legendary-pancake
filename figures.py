import turtle as ttl


def parallelogram(x, y, length, width):
    ttl.up()
    ttl.setposition(x, y)
    ttl.down()
    ttl.fillcolor('yellow')
    ttl.begin_fill()
    ttl.forward(length)
    ttl.right(135)
    ttl.forward(width)
    ttl.right(45)
    ttl.forward(length)
    ttl.right(135)
    ttl.forward(width)
    ttl.right(45)
    ttl.end_fill()


parallelogram(0, 0, 50, 30)


def rhomb(x, y, length, width):
    ttl.up()
    ttl.setposition(x, y)
    ttl.down()
    ttl.fillcolor('blue')
    ttl.begin_fill()
    ttl.forward(length)
    ttl.right(120)
    ttl.forward(width)
    ttl.right(60)
    ttl.forward(length)
    ttl.right(120)
    ttl.forward(width)
    ttl.right(60)
    ttl.end_fill()


rhomb(52, 52, 100, 75)


def rectangle(x, y, length, width):
    ttl.up()
    ttl.setposition(x, y)
    ttl.down()
    ttl.fillcolor('pink')
    ttl.begin_fill()
    ttl.forward(length)
    ttl.right(90)
    ttl.forward(width)
    ttl.right(90)
    ttl.forward(length)
    ttl.right(90)
    ttl.forward(width)
    ttl.right(90)
    ttl.end_fill()


rectangle(0, 0, 75, 150)


def trapezoid(x, y, bottom, top, left_border, right_border):
    ttl.up()
    ttl.setposition(x, y)
    ttl.down()
    ttl.fillcolor('orange')
    ttl.begin_fill()
    ttl.forward(left_border)
    ttl.right(90)
    ttl.forward(top)
    ttl.right(70)
    ttl.forward(right_border)
    ttl.right(110)
    ttl.forward(bottom)
    ttl.end_fill()

trapezoid(0, 0, 150, 99, 140, 149)

def square(x, y, a):
    ttl.up()
    ttl.setposition(x, y)
    ttl.down()
    ttl.fillcolor('purple')
    ttl.begin_fill()
    ttl.forward(a)
    ttl.right(90)
    ttl.forward(a)
    ttl.right(90)
    ttl.forward(a)
    ttl.right(90)
    ttl.forward(a)
    ttl.right(90)
    ttl.end_fill()
square(0,0,50)

def right_triangle(x,y,a):
    ttl.up()
    ttl.setposition(x, y)
    ttl.down()
    ttl.fillcolor('green')
    ttl.begin_fill()
    ttl.forward(a)
    ttl.left(90)
    ttl.forward(a)
    ttl.left(135)
    ttl.forward(a*(2**0.5))
    ttl.left(135)
    ttl.end_fill()
right_triangle(0,0,70)

def triangle(x,y,a):
    ttl.up()
    ttl.setposition(x,y)
    ttl.down()
    ttl.fillcolor('red')
    ttl.begin_fill()
    ttl.forward(a)
    ttl.left(120)
    ttl.forward(a)
    ttl.left(120)
    ttl.forward(a)
    ttl.left(120)
    ttl.end_fill()
triangle(0,0,100)
ttl.done