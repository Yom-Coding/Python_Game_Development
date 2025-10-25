import pgzrun
from random import randint


TITLE = "MY_GAME"
WIDTH = 650
HEIGHT = 400

paddle = Actor("paddle")
paddle.pos = WIDTH/2, HEIGHT-30

def place_circle():
    circle.x = randint (70, WIDTH - 70)
    circle.y = 20


circle = Actor("circle")
place_circle()

def draw():
    screen.fill("Blue")
    paddle.draw()
    circle.draw()



















pgzrun.go()