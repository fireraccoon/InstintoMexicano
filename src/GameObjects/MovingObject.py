import pygame

from Direction import Direction
from GameObject import GameObject


class MovingObject(GameObject):
    def __init__(self):
        GameObject.__init__(self)


        # MOVEMENTS PARAMETERS #
        self.direction = None
        self.speed_x = 6 # 6 pixels per tick
        self.speed_y = 10  # Jumping

        self.velocity_x = 0 # Negative means move left, positive means move right
        self.velocity_y = 0 # Negative means move up, positive means move down


        self.isGrounded = False

        self.isDead = False



    def update(self, walls):
        if self.isDead:
            return # No update if we are dead
        """ Move the object """
        # Move left/right
        self.rect.x += self.velocity_x

        # See if we hit anything
        hit_list_x = pygame.sprite.spritecollide(self, walls, False)
        for block in hit_list_x:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.velocity_x > 0:
                self.rect.right = block.rect.left
            elif self.velocity_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.velocity_y
        hit_list_y = pygame.sprite.spritecollide(self, walls, False)
        for block in hit_list_y:
            if self.velocity_y > 0:
                self.rect.bottom = block.rect.top
                self.isGrounded = True
                self.velocity_y = 1
            elif self.velocity_y < 0:
                self.rect.top = block.rect.bottom
                self.velocity_y = 1  # We fall because we hit our head

        if not hit_list_x and not hit_list_y:
            self.isGrounded = False


    def jump(self):
        if self.isGrounded:
            self.isGrounded = False
            self.velocity_y = -self.speed_y
            self.velocity_x *= .99



    # Player-controlled movement:
    def move_left(self):
        """ Called when the user hits the left arrow. """
        self.direction = Direction.LEFT
        self.velocity_x = -self.speed_x

    def move_right(self):
        """ Called when the user hits the right arrow. """
        self.direction = Direction.RIGHT
        self.velocity_x = self.speed_x

    def move_down(self):
        if not self.isGrounded:
            self.velocity_y += 5

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.velocity_x = 0