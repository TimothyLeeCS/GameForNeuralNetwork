import pygame
from ship import ShipCollection


pygame.init()
screen = pygame.display.set_mode((1600, 900))
pygame.display.set_caption('Dodge The Asteroids')

running = True
background = pygame.image.load('sprites/background.jpg')

ship = ShipCollection((800, 450))
group = pygame.sprite.RenderPlain()
group.add(ship)

vel = 4

while running == True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        ship.moveLeft(vel/2)

    if keys[pygame.K_RIGHT]:
        ship.moveRight(vel/2)
    
    if keys[pygame.K_UP]:
        ship.moveUp(vel)

    if keys[pygame.K_DOWN]:
        ship.moveDown(vel)
    
    group.draw(screen)
    pygame.display.update()
    pygame.display.flip()

pygame.quit()