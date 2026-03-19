import pygame
import pygame_manager as pm
from panel import MENU_Panel

class Menu(pm.states.State):

    def __init__(self):
        super().__init__("MENU")

        self.panel = MENU_Panel()
        self.bind_panel(self.panel)

