import arcade


class Pared(arcade.SpriteSolidColor):
    def __init__(self, width, hight, color, center_x, center_y):
        super().__init__(width, hight, color)
        self.center_x = center_x
        self.center_y = center_y

