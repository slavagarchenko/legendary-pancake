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
    ttl.seth(0)

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
    ttl.seth(0)


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
    ttl.seth(0)

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
    ttl.seth(0)

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
    ttl.seth(0)


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
    ttl.seth(0)


#def tangram():
    #right_triangle(0,0,50,135, 'green') #big
    #right_triangle(0,0,50,90, 'pink')#big
    #right_triangle(0.5*(2**0.5),0.5*(2**0.5),25,180,'red')#small
    #square(0,0,25,270,'orange')
    #right_triangle(0.5*(2**0.5)*25,0.5*(2**0.5)*25,25,0,'blue')#small
    #parallelogram(-0.5*(2**0.5)*25,-0.5*(2**0.5)*25,(2**0.5)*25,25,45,'yellow')
    #right_triangle((2**0.5)*25,-(2**0.5)*25,(2**0.5)*25,180,'purple')#middle
    #ttl.setheading(0)
#tangram()

def goose(x,y):
    right_triangle(x+0,y+0,50,225, 'green') #big
    right_triangle(x+25*(2**0.5),y+25*(2**0.5),50,45, 'orange')#big
    parallelogram(x-(2**0.5)*25+25,y+(2**0.5)*25+25,25,(2**0.5)*25,0,'blue')
    square(x-25*(2**0.5)+25,y+50+25*(2**0.5),25,0,'yellow')
    right_triangle(x-25*(2**0.5)+25,y+75+25*(2**0.5),25*(2**0.5),45,'red')#middle
    right_triangle(x,y-25,25,180,'purple')#small
    right_triangle(x+25*(2**0.5)+5*(21**0.5),y-10,25,112.5,'pink')#small
goose(-250,0)

def duck(x,y):
    right_triangle(x+0,y+25*(2**0.5),50,45, 'orange')#big
    right_triangle(x+25*(2**0.5),y+0,50,225, 'green') #big
    right_triangle(x+25*(2**0.5)-25,y-25,25*(2**0.5),225,'red')#middle
    parallelogram(x-(2**0.5)*12.5,y+37.5*(2**0.5),25,(2**0.5)*25,315,'blue')
    square(x-12.5*(2**0.5),y+37.5*(2**0.5),25,225,'yellow')
    right_triangle(x-25*(2**0.5),y+50*(2**0.5),25,45,'purple')#small
    right_triangle(x+37.5*(2**0.5),y+37.5*(2**0.5),25,45,'pink')#small
duck(0,0)

def bird(x,y):
    right_triangle(x+0,y+0,50,225, 'orange')#big
    right_triangle(x+25*(2**0.5)-50,y+25*(2**0.5),50,270, 'green') #big
    square(x+25*(2**0.5)-50,y+25*(2**0.5),25,180,'yellow')
    right_triangle(x+25*(2**0.5),y+50*(2**0.5),25*(2**0.5),0,'red')#middle
    parallelogram(x+12.5*(2**0.5),y+37.5*(2**0.5),(2**0.5)*25,25,270,'blue')
    right_triangle(x-25*(2**0.5),y+25*(2**0.5)-25,25,0,'purple')#small
    right_triangle(x+25*(2**0.5)-25,y+25*(2**0.5)-50,25,270,'pink')#small
bird(250,0)
