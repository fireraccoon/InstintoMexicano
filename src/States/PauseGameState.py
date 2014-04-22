from Colors import Colors
from State import State

import pygame

class PauseGameState(State):
    def __init__(self, sprites):
        State.__init__(self)
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
