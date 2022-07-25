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

vel = 10

clock = pygame.time.Clock()
dt = 0
game_time = 0

label_font = pygame.font.SysFont("monospace", 18)

def update_label(data, title, font, x, y, gameDisplay):
    label = font.render('{} {}'.format(title, data), 1, (0,255,0))
    gameDisplay.blit(label, (x, y))
    return y

def update_data_labels(gameDisplay, dt, game_time, font):
    y_pos = 10
    x_pos = 10
    gap = 20
    y_pos = update_label(round(game_time/1000,2),'Score', font, x_pos, y_pos + gap, gameDisplay)

while running == True:

    dt = clock.tick(30)
    game_time += dt

    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        ship.moveLeft(vel)

    if keys[pygame.K_RIGHT]:
        ship.moveRight(vel)
    
    if keys[pygame.K_UP]:
        ship.moveUp(vel)

    if keys[pygame.K_DOWN]:
        ship.moveDown(vel)
    
    
    group.update()
    group.draw(screen)
    update_data_labels(screen, dt, game_time, label_font)
    pygame.display.update()

pygame.quit()