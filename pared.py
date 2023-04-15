import arcade
import pymunk


class Pared(arcade.SpriteSolidColor):
    """Clase para crear un sprite de pared"""

    def __init__(self, width, hight, color, center_x, center_y, space: pymunk.Space):
        super().__init__(width, hight, color)
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = (center_x, center_y)
        shape = pymunk.Poly.create_box(body, (self.width, self.height))
        shape.elasticity = 0.8
        shape.friction = 10
        space.add(body, shape)
        self.body = body
        self.shape = shape

    def update(self):
        """Función de arcade que se ejecutara a cada frame para actualizar datos"""
        self.center_x = self.shape.body.position.x
        self.center_y = self.shape.body.position.y
