import pygame
import math

from Colors import Colors
from Direction import Direction
from GameObjects.GameObject import GameObject


class Explosive(GameObject):
    def __init__(self, shooter, angle):
        GameObject.__init__(self)

        self.shooter = shooter  # The GameObject responsible for the shoot
        self.angle = angle
        self.speed = 15

        self.velocity_x = 0  # Negative means move left, positive means move right
        self.velocity_y = 0  # Negative means move up, positive means move down

        self.gravity = 0

        self.width = 10
        self.height = 10

        self.damage = 5

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(Colors.BLACK)

        #Bounding box
        self.rect = self.image.get_rect()


    def update(self, targets):
        """ Move the player """
        # Move according to angle
        self.rect.x += self.speed * math.cos(math.radians(self.angle))
        self.rect.y += -self.speed * math.sin(math.radians(self.angle))+self.gravity

        self.gravity += 0.4


        # See if we hit anything

        # if self.shooter in targets
        #remove the shooter so we don't kill him
        targets.remove(self.shooter)

        hit_list = pygame.sprite.spritecollide(self, targets, True)
        for hit in hit_list:
            if hit != self.shooter:
                hit.isDead = True
                hit.hp -= self.damage
                targets.remove(hit)
        # We add the shooter back
        if self.shooter not in targets:
            targets.add(self.shooter)

