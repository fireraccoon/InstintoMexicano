import pygame
from Behaviours.EnnemyBehaviour import EnnemyBehaviour
from Colors import Colors
from GameObjects.Direction import Direction
from GameObjects.Gun import Gun
from GameObjects.Projectile import Projectile

from GameObjects.MovingObject import MovingObject


class Ennemy(MovingObject):

    def __init__(self, player):
        #pygame.sprite.Sprite.__init__(self)
        MovingObject.__init__(self)

        # MOVEMENT PARAMETERS
        self.speed_x = 2 # 6 pixels per tick


        self.width = 40
        self.height = 60
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(Colors.BLACK)

        #Bounding box
        self.rect = self.image.get_rect()

        # SHOOTING
        self.weapon = Gun()


        self.hp = 100


    def update(self, walls):
        MovingObject.update(self, walls)

    def shoot(self, angle):
        if self.isDead:
            return # We can't shoot if we are dead
        p = self.weapon.shoot(self, self.direction)
        if p:
            p.rect.x = self.rect.x+self.width
            p.rect.y = self.rect.y
            if self.direction == Direction.RIGHT:
                p.rect.x = self.rect.x+self.width
            else:
                p.rect.x = self.rect.x
        return p


