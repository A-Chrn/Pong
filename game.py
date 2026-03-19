import pygame
import pygame_manager as pm
from panel import Panel
from paddle import Paddle
from balle import Ball

class Game(pm.states.State):

    def __init__(self):
        super().__init__('game')

        self.panel = Panel()
        self.bind_panel(self.panel)
        self.score_max = 3
        pm.time.set_fps_limit(60)

    def update(self):
        self.paddle.update()
        self.paddle2.update()

    def reach(self, cote):
        if cote == "gauche":
            self.score2 += 1
            self.panel.score2.text=str(self.score2)
            self.reset()
        if cote == "droit":
            self.score1 += 1
            self.panel.score1.text=str(self.score1)
            self.reset()
        if self.score1 == self.score_max:
            pm.states.get_object("GAME_OVER").winner = 1
            pm.states.activate("GAME_OVER")
        if self.score2 == self.score_max:
            pm.states.get_object("GAME_OVER").winner = 2
            pm.states.activate("GAME_OVER")

    def toggle_freeze(self):
        if self.ball.is_active(): 
            self.ball.freeze()
        else : 
            self.ball.unfreeze()
        
        if self.paddle.is_active():
            self.paddle.freeze()
        else :
            self.paddle.unfreeze()

        if self.paddle2.is_active():
            self.paddle2.freeze()
        else :
            self.paddle2.unfreeze()
        
    def on_enter(self):
        self.score1 = 0
        self.score2 = 0
        self.panel.score2.text=str(self.score2)
        self.panel.score1.text=str(self.score1)
        self.ball = Ball(self, self.panel.centerx, self.panel.centery)
        self.paddle = Paddle(self, 40, pygame.K_z, pygame.K_s, (20, 50, 195))
        self.paddle2 = Paddle(self, self.panel.width - 40, pygame.K_UP, pygame.K_DOWN, (195, 50, 20))
        self.freeze()
        pm.inputs.when_any(self.unfreeze, once=True)
        pm.inputs.add_listener(pygame.K_ESCAPE, self.toggle_freeze) # Bonus : On peut mettre pause !
        
        return super().on_enter()
    
    def freeze(self):
        self.ball.freeze()
        self.paddle.freeze()
        self.paddle2.freeze()

    def unfreeze(self):
        self.ball.unfreeze()
        self.paddle.unfreeze()
        self.paddle2.unfreeze()

    def on_exit(self):
        self.ball.kill()
        self.paddle.kill()
        self.paddle2.kill()
        pm.inputs.remove_listener(pygame.K_ESCAPE, self.toggle_freeze) # Bonus : On peut mettre pause !
        return super().on_exit()
    
    def reset(self):
        self.ball.reset()
        self.paddle.reset()
        self.paddle2.reset()
        self.freeze()
        pm.inputs.when_any(self.unfreeze, once=True)