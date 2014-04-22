# A Level is a specialised State
import pygame
from States import State
from ViewPort import ViewPort


class Level(State.State):
    def __init__(self):
        State.State.__init__(self)

        self.sprites = pygame.sprite.Group()  # A Pygame Group of all the sprites to draw

        self.movingSprites = pygame.sprite.Group() # A Pygame Group of all the moving sprites other than bullets
        self.bullets = pygame.sprite.Group() # A PYgame Group of all the bullets
        self.platforms = pygame.sprite.Group()  # A Pygame Group of platforms

        self.player = None  #The Player

        # Physics
        self.gravity = 0.21875

        # Viewport
        self.viewport = ViewPort(350, 450, 100, 450)


    def init(self, engine):
        pass


    def shiftWorld(self, shift_x, shift_y):
        for sprite in self.sprites:
            sprite.rect.x += shift_x
            sprite.rect.y += shift_y

    def handleEvents(self, engine, events):
        pass

    def update(self, engine):
        pass

    def draw(self, engine):
        pass

    def cleanUp(self, engine):
        pass

    def pause(self, engine):
        pass

    def resume(self, engine):
        pass