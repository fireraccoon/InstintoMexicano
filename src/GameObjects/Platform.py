import pygame

from Colors import Colors
from GameObjects.GameObject import GameObject


class Platform(GameObject):
    """ Platform the user can jump on """

    def __init__(self, x, y, width, height):
        GameObject.__init__(self)

        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        self.image.fill(Colors.GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y