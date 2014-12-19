import pygame

from GoatEngine.Engine import GameState


class PlayGroundScene(GameState):
    def __init__(self):
        super(PlayGroundScene, self).__init__()
        self.gameObjects = []  # A list of gameObjects

    def init(self, engine):
        pass

    def handleEvents(self, engine, events):
        # Quit using (x) button window
        if pygame.QUIT in [event.type for event in events]:
            engine.exit()

    def update(self, engine, delta):
        pass

    def draw(self, engine):
        pass







