import pygame

from Components.GraphicsComponents import MercenarioGraphicsComponent, GraphicsComponent
from Components.InputComponents import PlayerInputComponent
from Components.Components import VelocityComponent, PhysicsComponent, PositionComponent
from GoatEngine.Engine import GameState
from GoatEngine.GameObject import GameObject


class PlayGroundScene(GameState):
    def __init__(self):
        super(PlayGroundScene, self).__init__()
        self.gameObjects = []  # A list of gameObjects

    def init(self, engine):
        hero = GameObject()
        hero.addComponent(PlayerInputComponent.ID, PlayerInputComponent())
        hero.addComponent(PhysicsComponent.ID, PhysicsComponent())
        hero.addComponent(VelocityComponent.ID, VelocityComponent())
        hero.addComponent(GraphicsComponent.ID, MercenarioGraphicsComponent())
        self.gameObjects.append(hero)


        babu = GameObject()
        pos = babu.components[PositionComponent.ID]
        pos.x = 50
        pos.y = 50
        babu.addComponent(PlayerInputComponent.ID, PlayerInputComponent())
        babu.addComponent(PhysicsComponent.ID, PhysicsComponent())
        babu.addComponent(VelocityComponent.ID, VelocityComponent())
        babu.addComponent(GraphicsComponent.ID, MercenarioGraphicsComponent())
        self.gameObjects.append(babu)





    def handleEvents(self, engine, events):
        # Quit using (x) button window
        if pygame.QUIT in [event.type for event in events]:
            engine.exit()
        self.events = events

    def update(self, engine, delta):
        [g.update(self, self.events) for g in self.gameObjects]

    def draw(self, engine):
        [g.render(engine.screen) for g in self.gameObjects]







