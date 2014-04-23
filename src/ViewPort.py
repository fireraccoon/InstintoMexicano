class ViewPort(object):
    def __init__(self, left_hotspot, right_hotspot, top_hotspot, bottom_hotspot ):
        """ hot spots are in pixels """
        self.min_x = left_hotspot
        self.max_x = right_hotspot
        self.min_y = top_hotspot
        self.max_y = bottom_hotspot

        # TIP to follow the player constantly invert left and right hotspot



    def update(self, level, player):

        shift_x = 0
        shift_y = 0

        #Player right side
        if player.rect.x >= self.max_x:
            diff = player.rect.x - self.max_x
            player.rect.x = self.max_x
            shift_x = -diff


        #Player left side
        if player.rect.x <= self.min_x:
            diff =self.min_x - player.rect.x
            player.rect.x = self.min_x
            shift_x = diff


        #Player bottom side
        if player.rect.y >= self.max_y:
            diff = player.rect.y - self.max_y
            player.rect.y = self.max_y
            shift_y = -diff

        if player.rect.y <= self.min_y:
            diff =self.min_y - player.rect.y
            player.rect.y = self.min_y
            shift_y = diff

        level.shiftWorld(shift_x, shift_y)