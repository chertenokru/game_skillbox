import math
import turtle

window = turtle.Screen()

window.bgpic("images/background.png")
window.setup(1200 + 5, 800 + 5)
window.screensize(1200, 800)
# window.tracer(2)
# draws.drawRandomFlowers()

BASE_X, BASE_Y = 0, -300


def calc_heading(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    length = (dx ** 2 + dy ** 2) ** 0.5
    cos_alpha = dx / length
    alpha = math.acos(cos_alpha)
    alpha = math.degrees(alpha)
    if dy < 0: alpha = -alpha
    return alpha


def launchMissle(x, y):
    missile = turtle.Turtle();
    missile.speed(0)
    missile.hideturtle()
    missile.penup()
    missile.color("white")
    missile.setpos(BASE_X, BASE_Y)
    missile.pendown()
    missile.setheading(calc_heading(BASE_X, BASE_Y, x, y))
    missile.showturtle()
    # missile.forward(500)
    # missile.shape('circle')
    # missile.shapesize(2)
    # missile.shapesize(3)
    # missile.shapesize(4)
    # missile.shapesize(5)
    # missile.clear()
    # missile.hideturtle()
    info = {'missile': missile, 'target': [x, y], 'state': 'launched', 'radius': 0}
    our_missiles.append(info)


window.onclick(launchMissle)
our_missiles = []

while True:
    window.update()

    # for num, missle in enumerate(our_missles):

    for info in our_missiles:
        missile = info['missile']
        if info['state'] == 'launched':
            missile.forward(4)
            target = info['target']
            if missile.distance(target[0], target[1]) < 20:
                missile.shape('circle')
                info['state'] = 'explode'
        elif info['state'] == 'explode':
            info['radius'] += 1
            if info['radius'] > 5:
                info['state'] = 'dead'
                missile.clear()
                missile.hideturtle()

            else:
                missile.shapesize(info['radius'])


    dead_missiles = [info for info in our_missiles if info['state'] == 'dead']
    for dead in dead_missiles:
        our_missiles.remove(dead)
