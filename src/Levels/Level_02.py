import pygame
from random import randint

from GameObjects.Characters import Player
from GameObjects.Characters.El_Mercenario import Mercenario
from GameObjects.Platform import Platform
from Colors import Colors
from ViewPort import ViewPort
from States.PauseGameState import PauseGameState
import Level as L
from util import getAngle
from States.State import State


class Level(State):
    def __init__(self):
        # GameObjects
        self.sprites = None  # A Pygame Group of all the sprites to draw
        self.moving_sprites = None  # A Pygame Group of all the movable sprites
        self.bullet_sprites = None
        self.platforms = None  # A Pygame Group of platforms
        self.player = None  #The Player

        # Physics
        self.gravity = 0.21875


        # Viewport
        self.viewport = ViewPort(350, 450, 100, 450)
        self.limit = 15000


    def init(self, engine):

        engine.log("Init Level 2")
        self.player = Mercenario()
        self.sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.moving_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()

        self.moving_sprites.add(self.player)

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

        self.sprites.add(self.player)



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
                        self.bullet_sprites.add(p)
                        self.sprites.add(p)

            self.player.control(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    engine.addState(PauseGameState(self.sprites))

                if event.key == pygame.K_r:
                    engine.changeState(Level())



    def update(self, engine):

        self.player.update(self.platforms)

        # Gravity
        self.applyGravity(self.player)


        # Bullets
        for s in self.bullet_sprites:
            s.update(self.moving_sprites)

        #SHIFTING THE WORLD
        self.viewport.update(self, self.player)

    def shiftWorld(self, shift_x, shift_y):

        for platform in self.platforms:
            platform.rect.x += shift_x
            platform.rect.y += shift_y

        for s in self.bullet_sprites:
            s.rect.x += shift_x
            s.rect.y += shift_y

    def applyGravity(self, sprite):
        """ Calculate effect of gravity and applies it to the sprite. """
        if not sprite.isGrounded:
            sprite.velocity_y *= 0.99
            sprite.velocity_y += self.gravity  # Progressive incrmenting of the velocity (acceleration)
            sprite.isGrounded = False

    def draw(self, engine):
        engine.screen.fill(Colors.BLUE)
        self.sprites.draw(engine.screen)

