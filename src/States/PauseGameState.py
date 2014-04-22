

import pygame
import Colors
from GoatEngine import GameState


class PauseGameGameState(GameState):
    def __init__(self, sprites):
        GameState.__init__(self)
        self.sprites = sprites


    def init(self, engine):
        pass


    def handleEvents(self, engine, events):
         for event in events:
             if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_ESCAPE:
                     engine.popState()
             if event.type == pygame.QUIT:
                engine.exit()

    def update(self, engine):
        pass

    def draw(self, engine):
        engine.screen.fill(Colors.WHITE)
        self.sprites.draw(engine.screen)
