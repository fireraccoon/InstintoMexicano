import pygame

from Colors import Colors
from GameObjects.Direction import Direction

from GameObjects.Gun import Gun


from GameObjects.MovingObject import MovingObject


class Player(MovingObject):



    def __init__(self):
        MovingObject.__init__(self)

        # VISUAL PARAMETERS #
        self.width = 40
        self.height = 60
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(Colors.RED)


        # POSITION AND BOUNDING BOX PARAMETERS #
        self.rect = self.image.get_rect()

        # MOVEMENTS PARAMETERS #
        self.direction = None

        self.speed_x = 6   # 6 pixels per tick
        self.speed_y = 10  # Jumping
        self.velocity_x = 0  # Negative means move left, positive means move right
        self.velocity_y = 0  # Negative means move up, positive means move down

        self.isGrounded = False


        # WEAPONS PARAMETERS #
        self.weapon = Gun()
        self.weapon.shootingDelay = 0 # No delay for the player

        # POINTS #
        self.hp = 100
        self.isDead = False



    def control(self, event):
        """ process an event and make the character move accordingly """

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.move_left()
                if event.key == pygame.K_d:
                    self.move_right()
                if event.key == pygame.K_s:
                    self.move_down()

                if event.key == pygame.K_w:
                    self.jump()

                if event.key == pygame.K_LSHIFT:
                    self.special()

        if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and self.velocity_x < 0:
                    self.stop()
                if event.key == pygame.K_d and self.velocity_x > 0:
                    self.stop()



    def shoot(self, angle):
        if self.isDead:
            return # We can't shoot if we are dead
        p = self.weapon.shoot(self, angle)
        if p:
            p.rect.x = self.rect.x+self.width
            p.rect.y = self.rect.y
            if self.direction == Direction.RIGHT:
                p.rect.x = self.rect.x+self.width
            else:
                p.rect.x = self.rect.x
        return p




    def special(self):
        pass







