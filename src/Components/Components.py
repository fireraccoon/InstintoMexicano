from abc import ABCMeta, abstractmethod


class Component:
    def __init__(self):
        pass

    def update(self, gameObject):
        pass




class PositionComponent(Component):
    """ Component used for GameObjects having a position in space
    """
    ID = 'POSITION'
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.isGrounded = True


class VelocityComponent(Component):
    """ A Components used for GameObjects moving in space
    """
    ID = 'VELOCITY'

    def __init__(self):
        super().__init__()
        self.vx = 0
        self.vy = 0


class HealthComponent(Component):
    """ Used for GameObjects having health points
    """
    ID = 'HEALTH'

    def __init__(self):
        super().__init__()
        self.amount = 0


class PhysicsComponent():
    __metaclass__ = ABCMeta
    ID = "PHYSICS"

    def __init__(self):
        pass

    @abstractmethod
    def update(self, gameObject):
        pos = gameObject.components[PositionComponent.ID]
        velo = gameObject.components[VelocityComponent.ID]
        pos.x += velo.vx

        pos.y += velo.vy



















