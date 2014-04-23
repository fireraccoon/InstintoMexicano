from GameObjects.GameObject import GameObject
from GameObjects.Explosive import Explosive


class GrenadeLauncher(GameObject):
    def __init__(self):
        GameObject.__init__(self)
        self.shootingDelay = 5
        self.shootCount = 0

    def shoot(self, shooter, angle):
        """ returns a bullet according to the shooting rate """
        p = None
        if self.shootCount < self.shootingDelay:
            self.shootCount += 1
        else:
            p = Explosive(shooter, angle)
            self.shootCount = 0

        return p