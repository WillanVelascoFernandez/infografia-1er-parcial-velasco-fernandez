import arcade


class Player(arcade.SpriteSolidColor):
    def __init__(self, width, hight, color, center_x, center_y):
        super().__init__(width, hight, color)
        self.center_x = center_x
        self.center_y = center_y
        self.speed = 1000
        self.score = 0

    def move_up(self, delta_time):
        self.center_y += self.speed * delta_time

    def move_down(self, delta_time):
        self.center_y -= self.speed * delta_time

    def colision_wall(self, wall):
        if self.collides_with_sprite(wall):
            return True
        return False

    def aumentar_score(self):
        self.score += 1
