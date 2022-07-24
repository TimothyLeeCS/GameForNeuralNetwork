import pygame
import os

class ShipCollection(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(ShipCollection, self).__init__()
        self.image = pygame.image.load(os.path.join('sprites','spaceship.png'))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        pass