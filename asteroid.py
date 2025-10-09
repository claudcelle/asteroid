from circleshape import CircleShape
import pygame
from constants import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self,screen,color = "white",width=OBJECTS_WIDTH):
        pygame.draw.circle(surface=screen,
                           color=color,
                           center=self.position,
                           radius=self.radius,
                           width=width)

    def update(self,dt):
        self.position += self.velocity * dt



