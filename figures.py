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
    ttl.done


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
    ttl.done


rhomb(52, 52, 100, 75)


def rectangle(x, y, length, width):
    ttl.up()
    ttl.setposition(x, y)
    ttl.down()
    ttl.fillcolor('black')
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
    ttl.done


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
    ttl.done

trapezoid(0, 0, 150, 99, 140, 149)

