import pygame
from ship import ShipCollection


pygame.init()
screen = pygame.display.set_mode((1600, 900))
pygame.display.set_caption('Dodge The Asteroids')

running = True
background = pygame.image.load('sprites/background.jpg')

width = 35
height = 40

vel = 10

ship = ShipCollection((800, 450))
group = pygame.sprite.RenderPlain()
group.add(ship)

while running == True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and ship_x>0:
        ship_x -= vel

    if keys[pygame.K_RIGHT] and ship_x<500-width:
        ship_x += vel
    
    if keys[pygame.K_UP] and ship_y>0:
        ship_y -= vel

    if keys[pygame.K_UP] and ship_y<500-width:
        ship_y += vel
    
    group.draw(screen)
    pygame.display.update()
    pygame.display.flip()

pygame.quit()