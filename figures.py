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
parallelogram (0, 0, 50, 30)

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