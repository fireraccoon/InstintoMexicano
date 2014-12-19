from abc import ABCMeta, abstractmethod

import pygame

from Components.Components import VelocityComponent, PositionComponent


class InputComponent:
    """ Used for GameObjects controllable by something (Whether AI or Human)
    """
    __metaclass__ = ABCMeta
    ID = "INPUT"

    def __init__(self):
        pass

    @abstractmethod
    def update(self, gameObject):
        pass


class PlayerInputComponent(InputComponent):
    """ Used for GameObjects controllable by the user with classic controls like WASD
    """

    def update(self, gameObject):
        for event in gameObject.events:
            moves = {
                pygame.K_a: self.moveLeft,
                pygame.K_d: self.moveRight,
                pygame.K_s: self.moveDown,
                pygame.K_w: self.jump
            }
            if event.type == pygame.KEYDOWN:
                try:
                    move = moves[event.key]
                    print("MOVE")
                    move(gameObject)
                    pos = gameObject.components[PositionComponent.ID]
                    print(pos.x, pos.y)
                except KeyError:
                    pass
            if event.type == pygame.KEYUP:
                velo = gameObject.components[VelocityComponent.ID]
                if event.key == pygame.K_a and velo.vx < 0:
                    self.stop(gameObject)
                if event.key == pygame.K_d and velo.vx > 0:
                    self.stop(gameObject)


    def moveLeft(self, gameObject):
        velo = gameObject.components[VelocityComponent.ID]
        velo.vx = -6

    def moveRight(self, gameObject):
        velo = gameObject.components[VelocityComponent.ID]
        velo.vx = 6

    def moveDown(self, gameObject):
        velo = gameObject.components[VelocityComponent.ID]
        pos = gameObject.components[PositionComponent.ID]
        if not pos.isGrounded:
            velo.vy += 5
        velo.vy += 5

    def jump(self, gameObject):
        velo = gameObject.components[VelocityComponent.ID]
        pos = gameObject.components[PositionComponent.ID]
        if pos.isGrounded:
            pos.isGrounded = False
            velo.vy = - 10  # SPEED
            velo.vx *= .99

    def stop(self, gameObject):
        velo = gameObject.components[VelocityComponent.ID]
        velo.vx = 0


class DummyInputComponent(InputComponent):

    def update(self, gameObject):
        # TODO AI CODE TO Automatically control the gameObject
        pass