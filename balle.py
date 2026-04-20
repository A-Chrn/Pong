import pygame_manager as pm
import math
import random

class Ball(pm.entities.CircleEntity) :
    def __init__(self, game, x, y):
        super().__init__((x, y), 20, zorder=0, panel="game")
        self.game = game

        self.center_init = (x, y)
        self.angle_min = 10
        self.angle_max = 40
        self.angle: float = math.radians((random.randint(self.angle_min, self.angle_max) if random.random() < 0.5 else random.randint(180 - self.angle_max, 180 - self.angle_min)) * random.choice((-1, 1)))
        self.celerity = 400
        self.vx = math.cos(self.angle)
        self.vy = -math.sin(self.angle)

    def update(self):
        
        self.celerity = min(1000, self.celerity + 1)
        self.x += self.vx * pm.time.scale_value(self.celerity)
        self.y += self.vy * pm.time.scale_value(self.celerity)

        # Rebond sur les bords verticaux
        if self.x - self.radius <= 0 :
            self.vx = -self.vx
            self.game.reach("gauche")
        
        if self.x + self.radius >= self.game.panel.width:
            self.vx = -self.vx
            self.game.reach("droit")

        # Rebond sur les bords horizontaux
        if self.y - self.radius <= 0 or self.y + self.radius >= self.game.panel.height:
            self.vy = -self.vy
            

        self.collisions(self.game.paddle)
        self.collisions(self.game.paddle2)
        

    def collisions(self, paddle):
        if self.colliderect(paddle.rect):
            normal = self.circle.rect_collision_normal(paddle.rect)
            self.bounce(normal)
            

    def bounce(self, normal):
        vector = pm.geometry.Vector(self.vx, self.vy)
        if vector @ normal > 0 :
            return
        vector -= vector @ normal * 2 * normal
        self.vx = vector.x
        self.vy = vector.y

        angle = math.atan2(-vector.y, vector.x)
        angle = (angle + math.pi) % (2 * math.pi) - math.pi

        sign = 1 if angle >= 0 else -1
        abs_angle = abs(angle)
        mini = math.radians(self.angle_min)
        maxi = math.radians(self.angle_max)
        if abs_angle > math.pi / 2: abs_angle = min(math.pi - mini, max(math.pi - maxi, abs_angle))
        else: abs_angle = min(mini, max(maxi, abs_angle))
        angle = sign * abs_angle

        vect = pm.geometry.Vector(math.cos(angle), -math.sin(angle)).normalized
        self.vx = vect.x
        self.vy = vect.y
            
    def reset(self):
        self.center = self.center_init
        self.celerity = 400


