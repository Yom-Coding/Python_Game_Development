import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.image.load("/Users/yompatel/Desktop/Jet Learn/Pro Game Developer/image/space.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

rocket_img = pygame.image.load("/Users/yompatel/Desktop/Jet Learn/Pro Game Developer/image/rocket.jpg")

clock = pygame.time.Clock()


rocket_x = WIDTH // 2
#print(rocket_x)
rocket_y = HEIGHT // 2
#print(rocket_y)
rocket_width = 50
rocket_height = 50


circle_radius = 15
circle_x = random.randint(circle_radius, WIDTH - circle_radius)
circle_y = random.randint(circle_radius, HEIGHT - circle_radius)


score = 0
font = pygame.font.SysFont(None, 36)


start_time = pygame.time.get_ticks()
time_limit = 30 

run = True
while run:
    screen.blit(background, (0, 0))

    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    #print("Mouse: " + str(mouse_x),str(mouse_y))
   
    rocket_x = mouse_x - 75
    rocket_y = mouse_y - 20
    #print("Rocket: " + str(rocket_x),str(rocket_y))


    screen.blit(rocket_img, (rocket_x, rocket_y))
    pygame.draw.circle(screen, (255, 0, 0), (circle_x, circle_y), circle_radius)

    #print ("Circle Original: " + str(circle_x),str(circle_y))

    if (mouse_x > circle_x - 10 and mouse_x < circle_x + 10 and
       mouse_y > circle_y - 10 and mouse_y < circle_y + 10):
  #      print("Mouse: " + str(mouse_x),str(mouse_y) + "Rocket: " + str(rocket_x),str(rocket_y) + "Circle Original: " + str(circle_x),str(circle_y) )
#    if rocket_x == circle_x - 75 and rocket_y == circle_y + 25 :
       
        score += 1
        circle_x = random.randint(circle_radius, WIDTH - circle_radius)
        circle_y = random.randint(circle_radius, HEIGHT - circle_radius)

    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    time_left = time_limit - elapsed_time
    if time_left < 0:
        time_left = 0

    timer_text = font.render("Time: " + str(time_left), True, (255, 255, 255))
    screen.blit(timer_text, (WIDTH - 120, 10))

    if time_left == 0:
        run = False

    pygame.display.update()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
