import pygame
from random import randint

from GameObjects.Characters import Player, Ennemy
from GameObjects.Characters.El_Mercenario import Mercenario
from GameObjects.Platform import Platform
from Colors import Colors

from States.PauseGameState import PauseGameGameState



from Level import Level as Lvl

from util import *


class Level(Lvl):
    def __init__(self):
        # GameObjects
        Lvl.__init__(self)
        self.limit = 15000

    def init(self, engine):

        engine.log("Init Level 1")
        self.player = Mercenario()
        self.movingSprites.add(self.player)
        self.sprites.add(self.player)

        self.ennemies = pygame.sprite.Group()
        for i in range(0):
            ennemy = Ennemy.Ennemy(self.player)
            ennemy.rect.x = randint(0, 1200)
            ennemy.rect.y = randint(0, 325)
            self.ennemies.add(ennemy)
            self.sprites.add(ennemy)
            self.moving_sprites.add(ennemy)

        self.movingSprites.add(self.player)

        # WALL AND PLATFORM PLACEMENTS
        wall = Platform(0, 550, self.limit, 50)
        self.platforms.add(wall)
        self.sprites.add(wall)

        wall = Platform(0, 250, 150, 50)
        self.platforms.add(wall)
        self.sprites.add(wall)

        wall = Platform(500, 450, 150, 50)
        self.platforms.add(wall)
        self.sprites.add(wall)

        wall = Platform(252, 176, 490-252, 50)
        self.platforms.add(wall)
        self.sprites.add(wall)

        wall = Platform(38, 430, 290-38, 50)
        self.platforms.add(wall)
        self.sprites.add(wall)

        wall = Platform(578, 320, 994-578, 50)
        self.platforms.add(wall)
        self.sprites.add(wall)

    def handleEvents(self, engine, events):
        for event in events:
            if event.type == pygame.QUIT:
                engine.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mousex, mousey = pygame.mouse.get_pos()
                    angle = getAngle(self.player.rect.x, self.player.rect.y, mousex, mousey)
                    p = self.player.shoot(angle)
                    if p:
                        self.bullets.add(p)
                        self.sprites.add(p)

            self.player.control(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    engine.addState(PauseGameState(self.sprites))

                if event.key == pygame.K_r:
                    engine.changeState(Level())

    def update_ennemy(self):
        # Ennemy Behaviour
        for ennemy in self.ennemies:
            ennemy.update(self.platforms)

            for s in self.movingSprites:
                if s == ennemy:
                    pass
                else:
                    self.ennemyGo(ennemy, s)

    def ennemyGo(self, ennemy, s):
        if ennemy.rect.x < s.rect.x:
            ennemy.move_right()

        if ennemy.rect.x > s.rect.x:
            ennemy.move_left()

        if ennemy.rect.y > s.rect.y:
                ennemy.jump()

        angle = getAngle(ennemy.rect.x, ennemy.rect.x, self.player.rect.x, self.player.rect.y)
        p = ennemy.shoot(angle)
        if p:
            self.bullets.add(p)
            self.sprites.add(p)

    def update(self, engine):

        # Player
        self.player.update(self.platforms)

        # Ennemies
        self.update_ennemy()

        # Bullets
        for s in self.bullets:
            s.update(self.movingSprites)

        # Gravity
        for sprite in self.movingSprites:
            self.applyGravity(sprite)


        alive = []
        for s in self.movingSprites:
            if not s.isDead:
                alive.append(s)


        #SHIFTING THE WORLD
        self.viewport.update(self, self.player)
        if len(alive) == 1:
            self.viewport.update(self, alive[-1])

    def shift_world(self, shift_x, shift_y):

        for sprite in self.sprites:
            if sprite is not self.player:
                sprite.rect.x += shift_x
                sprite.rect.y += shift_y

    def applyGravity(self, sprite):
        """ Calculate effect of gravity and applies it to the sprite. """
        if not sprite.isGrounded:
            sprite.velocity_y *= 0.99
            sprite.velocity_y += self.gravity  # Progressive incrementing of the velocity (acceleration)

    def draw(self, engine):
        engine.screen.fill(Colors.BLUE)
        self.sprites.draw(engine.screen)

