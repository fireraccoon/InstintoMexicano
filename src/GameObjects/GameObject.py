import pygame

from Colors import Colors


class GameObject(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


        self.width = 40
        self.height = 60
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(Colors.BLACK)

        #Bounding box
        self.rect = self.image.get_rect()
