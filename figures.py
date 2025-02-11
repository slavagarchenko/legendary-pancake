import turtle as ttl
# x,y - coordinates
# form_angle - the angle of the shape
def parallelogram(x, y, length, width, form_angle, color):
    ttl.up()
    ttl.setposition(x, y)
    ttl.down()
    ttl.fillcolor(color)
    ttl.begin_fill()
    ttl.right(form_angle)
    ttl.forward(length)
    ttl.right(135)
    ttl.forward(width)
    ttl.right(45)
    ttl.forward(length)
    ttl.right(135)
    ttl.forward(width)
    ttl.right(45)
    ttl.end_fill()

def rhomb(x, y, length, form_angle, color):
    ttl.up()
    ttl.setposition(x, y)
    ttl.down()
    ttl.fillcolor(color)
    ttl.begin_fill()
    ttl.right(form_angle)
    ttl.forward(length)
    ttl.right(120)
    ttl.forward(length)
    ttl.right(60)
    ttl.forward(length)
    ttl.right(120)
    ttl.forward(length)
    ttl.right(60)
    ttl.end_fill()


def rectangle(x, y, length, width, form_angle, color):
    ttl.up()
    ttl.setposition(x, y)
    ttl.down()
    ttl.fillcolor(color)
    ttl.begin_fill()
    ttl.right(form_angle)
    ttl.forward(length)
    ttl.right(90)
    ttl.forward(width)
    ttl.right(90)
    ttl.forward(length)
    ttl.right(90)
    ttl.forward(width)
    ttl.right(90)
    ttl.end_fill()


def trapezoid(x, y, bottom, top, left_border, right_border, form_angle, color):
    ttl.up()
    ttl.setposition(x, y)
    ttl.down()
    ttl.fillcolor(color)
    ttl.begin_fill()
    ttl.right(form_angle)
    ttl.forward(left_border)
    ttl.right(90)
    ttl.forward(top)
    ttl.right(70)
    ttl.forward(right_border)
    ttl.right(110)
    ttl.forward(bottom)
    ttl.end_fill()

def square(x, y, a, form_angle, color):
    ttl.up()
    ttl.setposition(x, y)
    ttl.down()
    ttl.fillcolor(color)
    ttl.begin_fill()
    ttl.right(form_angle)
    ttl.forward(a)
    ttl.right(90)
    ttl.forward(a)
    ttl.right(90)
    ttl.forward(a)
    ttl.right(90)
    ttl.forward(a)
    ttl.right(90)
    ttl.end_fill()

def right_triangle(x,y,a,form_angle, color):
    ttl.up()
    ttl.setposition(x, y)
    ttl.down()
    ttl.fillcolor(color)
    ttl.begin_fill()
    ttl.right(form_angle)
    ttl.forward(a)
    ttl.right(135)
    ttl.forward(a*(2**0.5))
    ttl.right(135)
    ttl.forward(a)
    ttl.right(90)
    ttl.end_fill()

def triangle(x,y,a, form_angle, color):
    ttl.up()
    ttl.setposition(x,y)
    ttl.down()
    ttl.fillcolor(color)
    ttl.begin_fill()
    ttl.right(form_angle)
    ttl.forward(a)
    ttl.right(120)
    ttl.forward(a)
    ttl.right(120)
    ttl.forward(a)
    ttl.right(120)
    ttl.end_fill()


def tangram():
    right_triangle(0,0,50,135, 'green') #big
    right_triangle(0,0,50,90, 'pink')#big
    right_triangle(0.5*(2**0.5),0.5*(2**0.5),25,180,'red')#small
    square(0,0,25,270,'orange')
    right_triangle(0.5*(2**0.5)*25,0.5*(2**0.5)*25,25,0,'blue')#small
    parallelogram(-0.5*(2**0.5)*25,-0.5*(2**0.5)*25,(2**0.5)*25,25,45,'yellow')
    right_triangle((2**0.5)*25,-(2**0.5)*25,(2**0.5)*25,180,'purple')#middle
    ttl.done()
tangram()

def goose():
    right_triangle(0,0,50,225, 'green') #big
    right_triangle(25*(2**0.5),25*(2**0.5),50,180, 'orange')#big
    parallelogram(25-(2**0.5)*25,(2**0.5)*25+25,25,(2**0.5)*25,315,'blue')
    square(25-25*(2**0.5),50+25*(2**0.5),25,0,'yellow')
    right_triangle(25-25*(2**0.5),75+25*(2**0.5),25*(2**0.5),45,'red')#middle
    right_triangle(0,-25,25,135,'purple')#small
    right_triangle(25*(2**0.5)+5*(21**0.5),-10,25,292.5,'pink')#small
goose()