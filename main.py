import random
import arcade
from pared import Pared
from pelota import Pelota
from player import Player

# definicion de constantes
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Ping Pong Retro"


class TransformWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.sprites = None
        self.paredes = None
        self.pared_arriba = None
        self.pared_abajo = None
        self.pelota = None
        self.pelotas = None
        self.goal_izquierda = None
        self.goal_derecha = None
        self.goals = None
        self.player1 = None
        self.player2 = None
        self.players = None
        self.keys_pressed = set()

    def setup(self):
        self.sprites = arcade.SpriteList()
        self.pelotas = arcade.SpriteList()
        self.paredes = arcade.SpriteList()
        self.goals = arcade.SpriteList()
        self.players = arcade.SpriteList()

        self.pared_arriba = Pared(SCREEN_WIDTH-100, 5, arcade.color.RED,
                                  (SCREEN_WIDTH/2), (SCREEN_HEIGHT - 80))
        self.paredes.append(self.pared_arriba)
        self.sprites.append(self.pared_arriba)

        self.pared_abajo = Pared(SCREEN_WIDTH-100, 5,
                                 arcade.color.RED, (SCREEN_WIDTH/2), (50))
        self.paredes.append(self.pared_abajo)
        self.sprites.append(self.pared_abajo)

        self.goal_izquierda = Pared(
            5, (SCREEN_HEIGHT-80-50), arcade.color.BLUE, (50), (((SCREEN_HEIGHT-80)+50)/2))
        self.sprites.append(self.goal_izquierda)

        self.goal_derecha = Pared(5, (SCREEN_HEIGHT-80-50), arcade.color.BLUE,
                                  (SCREEN_WIDTH-50), (((SCREEN_HEIGHT-80)+50)/2))
        self.sprites.append(self.goal_derecha)

        self.player1 = Player(30, 100, arcade.color.GREEN,
                              80, (((SCREEN_HEIGHT-80)+50)/2))
        self.players.append(self.player1)
        self.sprites.append(self.player1)

        self.player2 = Player(30, 100, arcade.color.GREEN,
                              (SCREEN_WIDTH-80), (((SCREEN_HEIGHT-80)+50)/2))
        self.players.append(self.player2)
        self.sprites.append(self.player2)

        self.pelota = Pelota("sprites/disco.png", 0.08, SCREEN_WIDTH/2,
                             ((SCREEN_HEIGHT-80)+50)/2)

        self.pelotas.append(self.pelota)
        self.sprites.append(self.pelota)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(f"{self.player2.score}/{self.player1.score}",
                         0,
                         SCREEN_HEIGHT-60,
                         arcade.color.YELLOW,
                         50,
                         width=SCREEN_WIDTH,
                         align="center"
                         )
        arcade.draw_text(f"R: retry\nSPACE: +1 discos\nT: -1 disco",
                         150,
                         SCREEN_HEIGHT-30,
                         arcade.color.YELLOW,
                         10,
                         width=SCREEN_WIDTH,
                         align="center"
                         )
        arcade.draw_text(f"Controls: UP and DOWN",
                         -50,
                         SCREEN_HEIGHT-50,
                         arcade.color.YELLOW,
                         10,
                         width=SCREEN_WIDTH,
                         align="right"
                         )
        arcade.draw_text(f"Controls: W and S",
                         50,
                         SCREEN_HEIGHT-50,
                         arcade.color.YELLOW,
                         10,
                         width=SCREEN_WIDTH,
                         align="left"
                         )
        self.sprites.draw()
        arcade.finish_render()

    def on_update(self, delta_time):
        if not (self.player1.colision_wall(self.pared_arriba)):
            if arcade.key.W in self.keys_pressed:
                self.player1.move_up(delta_time)
        if not (self.player1.colision_wall(self.pared_abajo)):
            if arcade.key.S in self.keys_pressed:
                self.player1.move_down(delta_time)

        if not (self.player2.colision_wall(self.pared_arriba)):
            if arcade.key.UP in self.keys_pressed:
                self.player2.move_up(delta_time)
        if not (self.player2.colision_wall(self.pared_abajo)):
            if arcade.key.DOWN in self.keys_pressed:
                self.player2.move_down(delta_time)

        for pelota in self.pelotas:
            pelota.change_direction_y(self.paredes)
            pelota.change_direction_x(self.players)
            if (pelota.goal(self.goal_izquierda)):
                self.player1.aumentar_score()
                pelota.remove_from_sprite_lists()
                self.new_pelota()
            if (pelota.goal(self.goal_derecha)):
                self.player2.aumentar_score()
                pelota.remove_from_sprite_lists()
                self.new_pelota()

        self.sprites.update()

    def new_pelota(self):
        self.pelota = Pelota("sprites/disco.png", 0.08, SCREEN_WIDTH/2,
                             ((SCREEN_HEIGHT-80)+50)/2)

        self.pelotas.append(self.pelota)
        self.sprites.append(self.pelota)

    def on_key_press(self, key, modifiers):
        if (key == arcade.key.SPACE):
            self.new_pelota()

        if (key == arcade.key.R):
            self.setup()
        if (key == arcade.key.T):
            self.pelotas[0].remove_from_sprite_lists()

        self.keys_pressed.add(key)

    def on_key_release(self, key, modifiers):
        self.keys_pressed.remove(key)


def main():

    app = TransformWindow()
    app.setup()
    arcade.run()


if __name__ == "__main__":
    main()
