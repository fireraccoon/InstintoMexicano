# A Level is a specialised State
from abc import abstractmethod
import pygame
from GoatEngine import GameState
from ViewPort import ViewPort


class Level(GameState):
    def __init__(self):
        GameState.__init__(self)

        self.sprites = pygame.sprite.Group()  # A Pygame Group of all the sprites to draw

        self.movingSprites = pygame.sprite.Group() # A Pygame Group of all the moving sprites other than bullets
        self.bullets = pygame.sprite.Group() # A PYgame Group of all the bullets
        self.platforms = pygame.sprite.Group()  # A Pygame Group of platforms

        self.player = None  #The Player

        # Physics
        self.gravity = 0.21875

        # Viewport
        self.viewport = ViewPort(350, 450, 100, 450)



    def shiftWorld(self, shift_x, shift_y):
        for sprite in self.sprites:
            sprite.rect.x += shift_x
            sprite.rect.y += shift_y

    @abstractmethod
    def init(self, engine):
        pass

    @abstractmethod
    def handleEvents(self, engine, events):
        pass

    @abstractmethod
    def update(self, engine):
        pass

    @abstractmethod
    def draw(self, engine):
        pass

    def cleanUp(self, engine):
        pass

    def pause(self, engine):
        pass

    def resume(self, engine):
        pass