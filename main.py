import pygame_manager as pm
import pygame
from game import Game
from game_over import Game_over
from Menu import Menu

class Main:
    def __init__(self):
        pm.init()
        self.menu = Menu()
        self.game = Game()
        self.game_over = Game_over()
        
        pm.states.activate("MENU")
        pm.screen.set_vsync(True)

    def update(self):
        pm.screen.clear((70, 70, 85))
        pm.states.update()
        
main = Main()
pm.run(main.update)