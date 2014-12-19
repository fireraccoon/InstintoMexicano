from abc import ABCMeta, abstractmethod

import pygame

from Components.Components import PositionComponent


class GraphicsComponent:
    ID = "GRAPHICS"
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, gameObject):
        """ Used to update the state of animation etc...
        :param gameObject:
        :return:
        """
        pass

    @abstractmethod
    def draw(self, gameObject, screen):
        """ Actually draws the graphics on screen
        """
        pass


class MercenarioGraphicsComponent(GraphicsComponent):
    def update(self, gameObject):
        pass

    def draw(self, gameObject, screen):
        pos = gameObject.components[PositionComponent.ID]
        w, h = gameObject.width, gameObject.height
        color = (0, 255, 0)
        pygame.draw.rect(screen, color, (pos.x, pos.y, w, h))


class MariachiGraphicsComponent(GraphicsComponent):
    def update(self, gameObject):
        pass

    def draw(self, gameObject, screen):
        pass

