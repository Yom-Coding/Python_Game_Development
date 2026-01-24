import pygame

pygame.init()

WIDTH = 900
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load("/Users/yompatel/Desktop/Jet Learn/Pro Game Developer/Space Invaders/images_and_assets/space_background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
spaceship_height = 50
spaceship_width = 50
divider = pygame.Rect(WIDTH/2 - 10, 0, 20, HEIGHT)
speed = 1
red_spaceship = pygame.image.load("/Users/yompatel/Desktop/Jet Learn/Pro Game Developer/Space Invaders/images_and_assets/spaceship_red.png")
red_spaceship = pygame.transform.scale(red_spaceship, (spaceship_height, spaceship_width))
red_spaceship = pygame.transform.rotate(red_spaceship, 90)
yellow_spaceship = pygame.image.load("/Users/yompatel/Desktop/Jet Learn/Pro Game Developer/Space Invaders/images_and_assets/spaceship_yellow.png")
yellow_spaceship = pygame.transform.scale(yellow_spaceship, (spaceship_height, spaceship_width))
yellow_spaceship = pygame.transform.rotate(yellow_spaceship, 270)
MAXIMUM_BULLETS = 2
RED_SPACESHIP_HIT = pygame.USEREVENT + 1
YELLOW_SPACESHIP_HIT = pygame.USEREVENT + 2

def red_spaceship_movement(red_rectangle, keys_pressed):
    if keys_pressed[pygame.K_a] and red_rectangle.left > 0:
        red_rectangle.x = red_rectangle.x - speed
    elif keys_pressed[pygame.K_d] and red_rectangle.right < divider.left:
        red_rectangle.x = red_rectangle.x + speed
    elif keys_pressed[pygame.K_w] and red_rectangle.top > 0:
        red_rectangle.y = red_rectangle.y - speed
    elif keys_pressed[pygame.K_s] and red_rectangle.bottom < HEIGHT:
        red_rectangle.y = red_rectangle.y + speed

def yellow_spaceship_movement(yellow_rectangle, keys_pressed):
    if keys_pressed[pygame.K_LEFT] and yellow_rectangle.left > divider.right:
        yellow_rectangle.x = yellow_rectangle.x - speed
    elif keys_pressed[pygame.K_RIGHT] and yellow_rectangle.right < WIDTH:
        yellow_rectangle.x = yellow_rectangle.x + speed
    elif keys_pressed[pygame.K_UP] and yellow_rectangle.top > 0:
        yellow_rectangle.y = yellow_rectangle.y - speed
    elif keys_pressed[pygame.K_DOWN] and yellow_rectangle.bottom < HEIGHT:
        yellow_rectangle.y = yellow_rectangle.y + speed

def bullets_movement(red_bullets, yellow_bullets, red_rectangle, yellow_rectangle):
    for bullet in red_bullets:
        bullet.x = bullet.x + 5
        if bullet.x > WIDTH:
            red_bullets.remove(bullet)
        if yellow_rectangle.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_SPACESHIP_HIT))
            red_bullets.remove(bullet)
    
    


def main():
    red_rectangle = pygame.Rect(200, HEIGHT/2, spaceship_width, spaceship_height)
    yellow_rectangle = pygame.Rect(700, HEIGHT/2, spaceship_width, spaceship_height)
    red_spaceship_bullets = []
    yellow_spaceship_bullets = []
    run = True
    while run:
        screen.blit(background, (0,0))
        screen.blit(red_spaceship, (red_rectangle.x, red_rectangle.y))
        screen.blit(yellow_spaceship, (yellow_rectangle.x, yellow_rectangle.y))
        pygame.draw.rect(screen, (255,255,255), divider)
        for bullet in red_spaceship_bullets:
            pygame.draw.rect(screen, (255,255,255), bullet)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and len(red_spaceship_bullets) < MAXIMUM_BULLETS:
                    red_bullet = pygame.Rect(red_rectangle.right, red_rectangle.centery, 10, 7)
                    red_spaceship_bullets.append(red_bullet)
            if event.type == YELLOW_SPACESHIP_HIT:
                print("Yellow Hit")

            
        all_keys = pygame.key.get_pressed()
        red_spaceship_movement(red_rectangle, all_keys)
        yellow_spaceship_movement(yellow_rectangle, all_keys)

        bullets_movement(red_spaceship_bullets, yellow_spaceship_bullets, red_rectangle, yellow_rectangle)
        
        

main()