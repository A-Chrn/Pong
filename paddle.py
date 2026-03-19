import pygame
import pygame_manager as pm

class Paddle(pm.entities.RectEntity):

    def __init__(self, game, x, key_up, key_down, color):
        self.game = game
        super().__init__(
            x=0,
            y=0,
            width=20,
            height=140,
            border_radius=10,
            zorder=1,
            panel="game"
        )
        self.center_init = (x, self.game.panel.centery)
        self.center = self.center_init
        self.key_up = key_up
        self.key_down = key_down
        self.color = color
        pm.inputs.add_listener(self.key_up, self.deplacement_haut, repeat=True)
        pm.inputs.add_listener(self.key_down, self.deplacement_bas, repeat=True)

    def deplacement_haut(self):
        self.centery = max(self.height / 2, self.centery - pm.time.scale_value(600))

    def deplacement_bas(self):
        self.centery = min(self.game.panel.height - self.height / 2, self.centery + pm.time.scale_value(600))

    def reset(self):
        self.center = self.center_init