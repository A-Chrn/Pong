import pygame
import pygame_manager as pm
from panel import GameOver_Panel

class Game_over(pm.states.State):

    def __init__(self):
        super().__init__("GAME_OVER")

        self.panel = GameOver_Panel()
        self.bind_panel(self.panel)
        self.winner = 1

    def on_enter(self):
        pm.inputs.add_listener(pygame.K_SPACE, self.replay)
        return super().on_enter()

    def replay(self):
        pm.states.activate("game")
        pm.inputs.remove_listener(pygame.K_SPACE, self.replay)