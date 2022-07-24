import pygame
import os

class ShipCollection(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(ShipCollection, self).__init__()
        self.image = pygame.image.load(os.path.join('sprites','spaceship.png'))
        self.image = pygame.transform.scale(self.image, (35, 40))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        pass

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveUp(self, speed):
        self.rect.y -= speed * speed/10

    def moveDown(self, speed):
        self.rect.y += speed * speed/10