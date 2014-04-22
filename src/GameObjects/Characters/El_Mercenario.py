from GameObjects.Characters.Player import Player
from Colors import Colors

import pygame


class Mercenario(Player):
    def __init__(self):
        Player.__init__(self)
        self.nb_jumps = 0

        # SPECIAL
        self.initial_speed_x = self.speed_x
        self.initial_speed_y = self.speed_y

        self.special_activated = False
        self.special_activation_time = 0

        self.special_speed_x = self.speed_x + 5
        self.special_speed_y = self.speed_y + 5
        self.special_duration = 5000  # 5 seconds


    def update(self, walls):
        self.checkSpecialTime()
        Player.update(self, walls)


    def checkSpecialTime(self):
        """ Checks if the special needs to be removed or not """
        if self.special_activated:
            if pygame.time.get_ticks() - self.special_activation_time >= self.special_duration:
                self.speed_x = self.initial_speed_x
                self.speed_y = self.initial_speed_y
                self.special_activated = False
                self.image.fill(Colors.RED)


    def special(self):
        if not self.special_activated:
            self.special_activated = True
            self.speed_x = self.special_speed_x
            self.speed_y = self.special_speed_y
            self.special_activation_time = pygame.time.get_ticks()
            self.image.fill(Colors.BLACK)



