import math
import random
import arcade
import pymunk


class Pelota(arcade.Sprite):
    """Clase para crear una pelota para el juego"""

    def __init__(self, image, scale, center_x, center_y, space: pymunk.Space):
        super().__init__(image, scale, center_x=center_x, center_y=center_y)
        self.speed = 1.5
        mass = 5
        radius = 20
        moment = pymunk.moment_for_circle(mass, 0, radius)
        body = pymunk.Body(mass, moment)
        body.position = (center_x, center_y)
        power = 1000
        impulse = power * \
            pymunk.Vec2d(random.choice([-1, 1]), random.choice([-1, 1]))
        body.apply_impulse_at_local_point(impulse)
        shape = pymunk.Circle(body, radius)
        shape.elasticity = 1.1
        shape.friction = 0
        shape.collision_type = 0
        space.add(body, shape)
        self.body = body
        self.shape = shape

    def update(self):
        """Función de arcade que se ejecutara a cada frame para actualizar datos"""
        self.center_x = self.shape.body.position.x
        self.center_y = self.shape.body.position.y
        self.angle = math.degrees(self.shape.body.angle)
        self.ajustar_velocidad_minima()
        self.ajustar_velocidad_maxima()

    def goal(self, goal):
        """Funcion que detecta si toco un goal"""
        if self.collides_with_sprite(goal):
            return True
        return False

    def ajustar_velocidad_minima(self):
        """Función para ajustar la minima velociad de movimiento"""
        if abs(self.shape.body.velocity.x) < 100:
            self.shape.body.velocity = pymunk.Vec2d(
                250, self.shape.body.velocity.y)

        if abs(self.shape.body.velocity.y) < 100:
            self.shape.body.velocity = pymunk.Vec2d(
                self.shape.body.velocity.x, 250)

    def ajustar_velocidad_maxima(self):
        """Función para ajustar la maxima velociad de movimiento"""
        if abs(self.shape.body.velocity.x) > 1300:
            self.shape.body.velocity = pymunk.Vec2d(
                1000, self.shape.body.velocity.y)

        if self.shape.body.velocity.y > 1300:
            self.shape.body.velocity = pymunk.Vec2d(
                self.shape.body.velocity.x, 1000)
