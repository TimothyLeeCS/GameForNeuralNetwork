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
        if (self.rect.x < 1560):
            self.rect.x += pixels

    def moveLeft(self, pixels):
        if (self.rect.x > 10):
            self.rect.x -= pixels

    def moveUp(self, pixels):
        if (self.rect.y > 10):
            self.rect.y -= pixels

    def moveDown(self, pixels):
        if (self.rect.y < 850):
            self.rect.y += pixels