import math
import turtle
import random

def drawRandomFlowers():
    for x in range(1, 10, 2):
        flovers(random.randint(-600, 600), random.randint(-600, 600), random.random() * 3.0 + 0.2)


def flovers(b_x=0, b_y=0, k=1.0):
    pen = turtle.Turtle()
    pen.speed(500)
    pen.right(90)
    pen.up()
    pen.setpos(b_x, b_y);
    pen.down()
    pen.color("#00ff00")
    pen.forward(200 * k)
    pen.up()
    pen.setpos(0 + b_x, 20 * k + b_y)
    pen.left(90)
    pen.down()
    pen.color("white")
    pen.fillcolor("yellow")
    pen.begin_fill()
    pen.circle(30 * k)
    pen.end_fill()

    for x in [-40, -35, -20, 0, 20, 35, 40]:
        pen.up()
        pen.setpos(x * k + b_x, b_y + math.sqrt(40 ** 2 - x ** 2) * k + 40 * k)
        pen.down()
        pen.fillcolor("red")
        pen.begin_fill()
        pen.circle(10 * k)
        pen.end_fill()
        pen.up()
        pen.setpos(x * k + b_x, b_y - math.sqrt(40 ** 2 - x ** 2) * k + 40 * k)
        pen.down()
        pen.begin_fill()
        pen.circle(10 * k)
        pen.end_fill()
    pen.up()
    pen.setpos(0 + b_x, 0 + b_y)
    pen.right(90)
    pen.color("#00ff00")
    pen.setpos(0 + b_x, -150 * k + b_y)
    pen.down()
    pen.begin_fill()
    pen.setpos(-40 * k + b_x, -80 * k + b_y)
    pen.setpos(-110 * k + b_x, -50 * k + b_y)
    pen.setpos(-80 * k + b_x, -120 * k + b_y)
    pen.setpos(0 + b_x, -150 * k + b_y)
    pen.end_fill()

    pen.setpos(0 + b_x, 0 + b_y)
    pen.right(90)
    pen.color("#0fff0f")
    pen.setpos(0 + b_x, -100 * k + b_y)
    pen.down()
    pen.begin_fill()
    pen.setpos(40 * k + b_x, -30 * k + b_y)
    pen.setpos(110 * k + b_x, 0 + b_y)
    pen.setpos(80 * k + b_x, -70 * k + b_y)
    pen.setpos(0 + b_x, -100 * k + b_y)
    pen.end_fill()
    pen.hideturtle()
