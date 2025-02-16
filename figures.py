# Case-study #1
# Developers: Garchenko V.,Gaberman A., Rahimov I.

import turtle as ttl
# x,y - coordinates
# form_angle - the angle of the shape
ttl.tracer(0)
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



def goose(x,y):
    right_triangle(x+0, y+0, 50, 225, 'green') #big
    right_triangle(x+25*(2**0.5), y+25*(2**0.5), 50, 45, 'orange')#big
    parallelogram(x-(2**0.5)*25+25, y+(2**0.5)*25+25, 25, (2**0.5)*25, 0, 'blue')
    square(x-25*(2**0.5)+25,y+50+25*(2**0.5), 25, 0, 'yellow')
    right_triangle(x-25*(2**0.5)+25, y+75+25*(2**0.5), 25*(2**0.5), 45, 'red')#middle
    right_triangle(x, y-25, 25, 180, 'purple')#small
    right_triangle(x+25*(2**0.5)+5*(21**0.5), y-10, 25, 112.5, 'pink')#small
goose(-250,250)

def duck(x,y):
    right_triangle(x+25*(2**0.5)-10, y+0, 50, 225, 'green') #big
    right_triangle(x-10, y+25*(2**0.5), 50, 45, 'orange')#big
    parallelogram(x-(2**0.5)*12.5-10, y+37.5*(2**0.5), 25, (2**0.5)*25, 315, 'blue')
    square(x-12.5*(2**0.5)-10, y+37.5*(2**0.5), 25, 225, 'yellow')
    right_triangle(x+25*(2**0.5)-35, y-25, 25*(2**0.5), 225, 'red')#middle
    right_triangle(x-25*(2**0.5)-10, y+50*(2**0.5), 25, 45, 'purple')#small
    right_triangle(x+37.5*(2**0.5)-10, y+37.5*(2**0.5), 25, 45, 'pink')#small
duck(0,250)

def horse(x,y):
    right_triangle(x+0, y+50, 50, 0, 'green') #big
    right_triangle(x-25*(2**0.5), y-25*(2**0.5)+50, 50, 315, 'orange')#big
    parallelogram(x-25*(2**0.5)+10, y-25*(2**0.5)-5*(21**0.5)+50, (2**0.5)*25, 25, 112.5, 'blue')
    square(x+0, y+50, 25, 270, 'yellow')
    right_triangle(x+25, y+100, 25*(2**0.5), 45, 'red')#middle
    right_triangle(x+50, y+50, 25, 45, 'purple')#small
    right_triangle(x+0, y-25, 25, 270, 'pink')#small
horse(250,250)

def swan(x,y):
    right_triangle(x+25, y+15, 50, 45, 'green') #big
    right_triangle(x-25*(2**0.5)+25, y-25*(2**0.5)+15, 50, 225, 'orange')#big
    parallelogram(x+(2**0.5)*25, y-25*(2**0.5)+65, (2**0.5)*25, 25, 45,'blue')
    square(x+25*(2**0.5), y+65-25*(2**0.5), 25, 180, 'yellow')
    right_triangle(x-25*(2**0.5), y-25*(2**0.5)+40, 25*(2**0.5), 45, 'red')#middle
    right_triangle(x+25*(2**0.5)+25, y-25*(2**0.5)+40, 25, 90, 'purple')#small
    right_triangle(x+25*(2**0.5), y+65-25*(2**0.5), 25, 270, 'pink')#small
swan(-250,0)

def tangram(x,y):
    right_triangle(x+0, y+10, 50, 225, 'green') #big
    right_triangle(x+0, y+10, 50, 135, 'orange')#big
    parallelogram(x-12.5*(2**0.5), y-12.5*(2**0.5)+10, (2**0.5)*25, 25, 0, 'blue')
    square(x+0, y+10, 25, 315, 'yellow')
    right_triangle(x+25*(2**0.5), y-25*(2**0.5)+10, 25*(2**0.5), 180, 'red')#middle
    right_triangle(x+0, y+10, 25, 45, 'purple')#small
    right_triangle(x+12.5*(2**0.5), y+12.5*(2**0.5)+10, 25, 315, 'pink')#small
tangram(0,0)

def bird(x,y):
    right_triangle(x+25*(2**0.5)-50, y+25*(2**0.5)-10, 50, 270, 'green') #big
    right_triangle(x+0, y-10, 50, 225, 'orange')#big
    parallelogram(x+12.5*(2**0.5), y+37.5*(2**0.5)-10, (2**0.5)*25, 25, 270, 'blue')
    square(x+25*(2**0.5)-50, y+25*(2**0.5)-10, 25, 180, 'yellow')
    right_triangle(x+25*(2**0.5), y+50*(2**0.5)-10, 25*(2**0.5), 0, 'red')#middle
    right_triangle(x-25*(2**0.5), y+25*(2**0.5)-35, 25, 0, 'purple')#small
    right_triangle(x+25*(2**0.5)-25, y+25*(2**0.5)-60, 25, 270, 'pink')#small
bird(250,0)

def bull(x,y):
    right_triangle(x+35, y-5, 50, 0, 'green')  # big
    right_triangle(x+20, y-30, 50, 135, 'orange')  # big
    parallelogram(x+60, y-30, 25, (2**0.5)*25, -45, 'blue')
    square(x-40, y+30, 25, 0, 'yellow')
    right_triangle(x+35 , y-10, 25*(2**0.5), 90, 'red')  # middle
    right_triangle(x-58, y+30, 25, 315, 'purple')  # small
    right_triangle(x+3, y+30, 25, 135, 'pink')  # small
bull(-250,-250)

def goat(x,y):
    right_triangle(x+10, y+5, 50, 45, 'green')  # big
    right_triangle(x+70, y-5, 50, 90, 'orange')  # big
    parallelogram(x-20, y+45, 25, (2**0.5)*25, 0, 'blue')
    square(x-10, y+20, 25, 45, 'yellow')
    right_triangle(x-45, y +20, 25*(2**0.5), 0, 'red')  # middle
    right_triangle(x+88, y+5, 25, 135, 'purple')  # small
    right_triangle(x+0, y-30, 25, 90, 'pink')  # small
goat(0,-250)

def knight(x,y):
    right_triangle(x-40, y-30, 50, 270, 'green')  # big
    right_triangle(x+35, y-5, 50, 90, 'orange')  # big
    parallelogram(x+60, y-30, 25, (2 ** 0.5) * 25, 90, 'blue')
    square(x+20, y+60, 25, 45, 'yellow')
    right_triangle(x+20, y-5, 25*(2 ** 0.5), 180, 'red')  # middle
    right_triangle(x-40, y-5, 25, 180, 'purple')  # small
    right_triangle(x-40, y-30, 25, 0, 'pink')  # small
knight(250,-250)

ttl.done()