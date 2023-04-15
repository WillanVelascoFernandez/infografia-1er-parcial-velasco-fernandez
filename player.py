import arcade
import pymunk


class Player(arcade.SpriteSolidColor):
    """Clase para crear a un sprite jugador"""

    def __init__(self, width, hight, color, center_x, center_y, space: pymunk.Space):
        super().__init__(width, hight, color)
        self.center_x = center_x
        self.center_y = center_y
        self.speed = 1000
        self.score = 0
        body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        body.position = (self.center_x, self.center_y)
        shape = pymunk.Poly.create_box(body, (self.width, self.height))
        shape.elasticity = 1.12
        shape.friction = 1
        space.add(body, shape)
        self.body = body
        self.shape = shape

    def update(self):
        """Función de arcade que se ejecutara a cada frame para actualizar datos"""
        self.shape.body.position = (self.center_x, self.center_y)

    def move_up(self, delta_time):
        """Función para mover hacia arriba al jugador"""
        self.center_y += self.speed * delta_time

    def move_down(self, delta_time):
        """Función para mover hacia abajo al jugador"""
        self.center_y -= self.speed * delta_time

    def colision_wall(self, wall):
        """Funcion si detecta si golpea contra un sprite pared"""
        if self.collides_with_sprite(wall):
            return True
        return False

    def aumentar_score(self):
        """Función para aumentar el score del jugador"""
        self.score += 1
