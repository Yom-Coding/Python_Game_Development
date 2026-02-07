import pygame
import random
import time

pygame.init()

WIDTH = 600
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.image.load("/Users/yompatel/Desktop/Jet Learn/Pro Game Developer/image/space.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

rocket = pygame.image.load("/Users/yompatel/Desktop/Jet Learn/Pro Game Developer/image/rocket.jpg")

clock = pygame.time.Clock()


rocket_x = WIDTH//2
rocket_y = 100
rocket_width = 50
rocket_height = 50


circle_radius = 20
circle_x = random.randint(circle_radius, WIDTH - circle_radius)
circle_y = HEIGHT

rocket_rect = pygame.Rect(rocket_x, rocket_y, rocket_width, rocket_height)
score = 0
font = pygame.font.SysFont(None, 36)

asteroids = []
asteroid_radius = 20
asteroid_speed = 3
last_spawn = pygame.time.get_ticks()

start_time = time.time()

run = True
while run:
    screen.blit(background, (0, 0))
    screen.blit(rocket, (rocket_rect.x, rocket_rect.y))
    
    
    mouse_x, mouse_y = pygame.mouse.get_pos()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()




     
    

pygame.quit()