import pygame_manager as pm
import pygame
import balle

class Panel(pm.panels.Panel):
    def __init__(self):
        super().__init__("game", rect=pygame.Rect(0, 0, 1440, 1080), centered=True)
        self.background = (0, 0, 0)

        self.score1 = pm.ui.Text(
            x = self.width*0.15,
            y = self.height*0.1, 
            anchor="center",
            text = str(0),
            font_color= (255, 255, 255),
            font_size = 100,
            bold = True,
            panel = str(self),
            auto = False
        )

        self.score2 = pm.ui.Text(
            x = self.width*0.85,
            y = self.height*0.1, 
            anchor="center",
            text = str(0),
            font_color= (255, 255, 255),
            font_size = 100,
            bold = True,
            panel = str(self),
            auto = False
        )
    
    def draw_back(self, surface):
        surface.fill(self.background)
        surface.blit(self.score1.surface, self.score1.rect)
        surface.blit(self.score2.surface, self.score2.rect)
        return super().draw_back(surface)
    
class GameOver_Panel(pm.panels.Panel):
    def __init__(self):
        super().__init__("GAME_OVER", rect=pygame.Rect(0, 0, 1420, 1080), centered=True)
        self.background = (0, 0, 255)

        self.victoire = pm.ui.Text(
            x=self.centerx,
            y=self.height * 0.4,
            text="",
            anchor="center",
            font_size=100,
            font_color=(255, 0, 0),
            gradient=True,
            gradient_color=(255, 255, 0),
            gradient_fluctuation=True,
            panel=str(self)
        )

        self.restart = pm.ui.Text(
            x=self.centerx,
            y=self.height * 0.6,
            text="Press SPACE to restart",
            anchor="center",
            font_size=60,
            font_color=(0, 0, 0),
            panel=str(self)
        )

    def draw_back(self, surface):
        surface.fill(self.background)
        return super().draw_back(surface)
    
    def on_enter(self):
        self.victoire.text = f"LE VAINQUEUR EST JOUEUR {pm.states.get_object('GAME_OVER').winner}"
        return super().on_enter()
    
class MENU_Panel(pm.panels.Panel):
    def __init__(self):
        super().__init__("MENU", rect=pygame.Rect(0, 0, 1920, 1080), centered=True)
        self.background = (0, 0, 0)

        # Les polices d'écritures
        self.font_big = pygame.font.SysFont("arial", 120, bold=True)

        self.boutton = pm.ui.RectButton(
            x = self.centerx, 
            y = self.centery, 
            anchor = "center",
            width = 400, 
            height = 120, 
            filling_color = (0, 255, 0), 
            filling_color_hover = (0, 220, 0),
            border_radius = 20,
            text = "JOUER",
            font_color=(0, 0, 0),
            callback = self.handle_start, 
            panel = str(self)
            )
    
    def draw_back(self, surface):
        surface.fill(self.background)
        
        # Titre
        titre = self.font_big.render("BIENVENUE SUR PONG", True, (255, 255, 255))
        titre_rect = titre.get_rect(center=(self.centerx, self.centery - 400))
        surface.blit(titre, titre_rect)

        return super().draw_back(surface)
    
    def handle_start(self):
        pm.states.activate("game")