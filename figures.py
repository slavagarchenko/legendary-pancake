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

def bull(x,y):
    parallelogram(x + 0, y + 0, 25, (2 ** 0.5) * 25, -45, 'blue')
    right_triangle(x - 25, y + 25, 50, 0, 'green')  # big
    right_triangle(x - 25 , y  + 20, 25 * (2 ** 0.5), 90, 'red')  # middle
    right_triangle(x - 40, y + 0, 50, 135, 'orange')  # big
    square(x - 100, y + 50, 25, 0, 'yellow')
    right_triangle(x - 118, y + 60, 25, 315, 'purple')  # small
    right_triangle(x - 57, y + 60, 25, 135, 'pink')  # small
bull(-200, -300)

def goat(x,y):
    parallelogram(x + 0,y+0,25,(2**0.5)*25,0,'blue')
    right_triangle(x - 25, y - 25, 25 * (2 ** 0.5), 0, 'red')  # middle
    square(x + 10, y - 25, 25, 45, 'yellow')
    right_triangle(x + 30, y - 40, 50, 45, 'green')  # big
    right_triangle(x + 90, y - 50, 50, 90, 'orange')  # big
    right_triangle(x + 108, y - 40, 25, 135, 'purple')  # small
    right_triangle(x + 20, y - 75, 25, 90, 'pink')  # small
goat(-30, -225)

def knight(x,y):
    right_triangle(x + 0, y + 25, 25, 180, 'purple')  # small
    right_triangle(x + 0, y + 0, 50, 270, 'green')  # big
    right_triangle(x - 0, y + 0, 25, 0, 'pink')  # small
    right_triangle(x + 75, y + 25, 50, 90, 'orange')  # big
    parallelogram(x + 100, y + 0, 25, (2 ** 0.5) * 25, 90, 'blue')
    right_triangle(x + 60, y + 25, 25 * (2 ** 0.5), 180, 'red')  # middle
    square(x + 60, y + 90, 25, 45, 'yellow')
knight(200, -300)
