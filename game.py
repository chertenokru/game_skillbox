import os
import random
import turtle

window = turtle.Screen()

BASE_PATH = os.path.dirname(__file__)
window.bgpic(os.path.join(BASE_PATH, "images", "background.png"))
window.setup(1200 + 5, 800 + 5)
window.screensize(1200, 800)
# window.tracer(2)
# draws.drawRandomFlowers()

BASE_X, BASE_Y = 0, -300


# pen.toward(x,y) - аналог
# def calc_heading(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     length = (dx ** 2 + dy ** 2) ** 0.5
#     cos_alpha = dx / length
#     alpha = math.acos(cos_alpha)
#     alpha = math.degrees(alpha)
#     if dy < 0: alpha = -alpha
#     return alpha


def createMissle(color, x, y, x2, y2):
    missile = turtle.Turtle()
    missile.speed(0)
    missile.hideturtle()
    missile.penup()
    missile.color(color)
    missile.setpos(x, y)
    missile.pendown()
    missile.setheading(missile.towards(x2, y2))
    missile.showturtle()
    return {'missile': missile, 'target': [x2, y2], 'state': 'launched', 'radius': 0}


def fire_missle(x, y):
    our_missiles.append(createMissle("white", BASE_X, BASE_Y, x, y))


def fire_enemy_missle():
    y = 400
    x = random.randint(-600, 600)
    enemy_missiles.append(createMissle("red", x, y, BASE_X, BASE_Y))


def move_missale(missiles):
    # for num, missle in enumerate(missles):
    for info in missiles:
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
        elif info['state'] == 'dead':
            missile.clear()
            missile.hideturtle()

    dead_missiles = [info for info in missiles if info['state'] == 'dead']
    for dead in dead_missiles:
        missiles.remove(dead)

def check_enemy_count():
    if len(enemy_missiles) < 5:
        fire_enemy_missle()


def check_interceptions():
    for our_info in our_missiles:
        if our_info['state'] != 'explode':
            continue
        our_missile = our_info['missile']
        for enemy_info in enemy_missiles:
            enemy_missile = enemy_info['missile']
            if enemy_missile.distance(our_missile.xcor(),our_missile.ycor()) < 20:
                enemy_info['state'] = 'dead'


window.onclick(fire_missle)
our_missiles = []
enemy_missiles = []








while True:
    window.update()
    check_enemy_count()
    check_interceptions()
    move_missale(our_missiles)
    move_missale(enemy_missiles)
