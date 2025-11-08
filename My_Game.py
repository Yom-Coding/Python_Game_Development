import pgzrun
from random import randint


TITLE = "MY_GAME"
WIDTH = 650
HEIGHT = 400

paddle = Actor("paddle")
paddle.pos = WIDTH/2, HEIGHT-30

score = 0
ball_direction = 1 
x_offset = 0
lives = 3
game_over = False
speed = 5
last_speed_up = 0

def place_circle():
    circle.x = randint (70, WIDTH - 70)
    circle.y = 20


circle = Actor("circle")
place_circle()



def draw():
    screen.fill("Blue")
    if not game_over:
        paddle.draw()
        circle.draw()
        screen.draw.text(f"Score : {score}", (10,10))
        screen.draw.text(f"Lives : {lives}", (WIDTH - 100 ,10))
    else:
        screen.draw.text("The Game Is Over. Your Score was " + str(score), center = (WIDTH // 2, HEIGHT // 2), color = 'white')

def update():
    global ball_direction, score, x_offset, lives, game_over, speed, last_speed_up
    if keyboard.left:
        paddle.x = paddle.x - 10
    
    if keyboard.right:
        paddle.x = paddle.x + 10

    circle.y = circle.y + speed * ball_direction
    circle.x = circle.x  + x_offset

    if circle.colliderect(paddle):
        ball_direction = -1
        score = score + 1
        x_offset = circle.x - paddle.x
        x_offset = x_offset * 0.1

    if circle.y <= 0:
        ball_direction = 1

    if circle.x <= 0 or circle.x >= WIDTH:
        x_offset = x_offset * -1

    if circle.y >= HEIGHT:
        lives = lives - 1
        circle.y = 0
        circle.x = randint (70, WIDTH - 70)

    if lives == 0:
        game_over = True

    if score // 10 > last_speed_up:
        print("HI")
        speed = speed + 2
        last_speed_up = score // 10





 
 
        




















pgzrun.go()