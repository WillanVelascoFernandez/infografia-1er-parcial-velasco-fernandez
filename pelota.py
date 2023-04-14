import random
import arcade


class Pelota(arcade.Sprite):
    def __init__(self, image, scale, center_x, center_y):
        super().__init__(image, scale, center_x=center_x, center_y=center_y)
        self.speed = 1.5
        self.change_x = random.choice([-4, -3, -2, 4, 3, 2])
        self.change_y = random.choice([-4, -3, -2, 4, 3, 2])

    def update(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def change_direction_y(self, walls):
        if self.collides_with_list(walls):
            self.change_y *= -1

    def change_direction_x(self, players):
        if self.collides_with_list(players):
            self.change_x *= -1
            self.speed += 0.3

    def goal(self, goal):
        if self.collides_with_sprite(goal):
            return True
        return False
