import pgzrun
from random import randint

WIDTH = 300
HEIGHT = 300
TITLE = "Multiple Rectangles"

def draw():
    width = WIDTH
    height = HEIGHT - 200

    r = 255
    g = 0
    b = randint (120,255)

    for i in range(12):
        rect = Rect((0, 0), (width, height))
        rect.center = 150, 150
        screen.draw.rect(rect, (r, g, b))

        width -= 10
        height += 10

        b -= 10
        g += 10

pgzrun.go()

