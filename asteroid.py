from circleshape import CircleShape
import pygame
from constants import *
import random

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

    def split(self):
        self.kill()
        if self.radius<ASTEROID_MIN_RADIUS:
            return
        else:
            self.spawn_pair()


    def spawn_pair(self):
        theta = random.uniform(20,50)
        son_1 = Asteroid(self.position.x+self.radius/4,
                         self.position.y,
                         self.radius/2)
        son_2 = Asteroid(self.position.x+self.radius/4,
                         self.position.y,
                         self.radius/2)
        son_1.velocity = self.velocity.rotate(theta)
        son_2.velocity = self.velocity.rotate(-theta)

